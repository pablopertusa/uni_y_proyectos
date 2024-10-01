import 'dart:async';
import 'package:auth/screens/home.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

class VerifyPage extends StatefulWidget {
  const VerifyPage({super.key});

  @override
  State<VerifyPage> createState() => _VerifyPageState();
}

class _VerifyPageState extends State<VerifyPage> {
  bool isVerified = false;
  bool canResend = false;
  Timer? timer;

  @override
  void initState() {
    super.initState();
    isVerified = FirebaseAuth.instance.currentUser!.emailVerified;
    if (!isVerified) {
      sendVerificationEmail();

      timer = Timer.periodic(const Duration(seconds: 5), (_) {
        checkEmailVerified();
      });
    }
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  Future checkEmailVerified() async {
    await FirebaseAuth.instance.currentUser!.reload();
    if (FirebaseAuth.instance.currentUser!.emailVerified) {
      setState(() {
        isVerified = true;
      });
      timer?.cancel();
    }
  }

  Future sendVerificationEmail() async {
    try {
      await FirebaseAuth.instance.currentUser!.sendEmailVerification();
      setState(() {
        canResend = false;
      });
      await Future.delayed(const Duration(seconds: 60));
      setState(() {
        canResend = true;
      });
    } catch (e) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(25),
                topRight: Radius.circular(25),
              ),
            ),
            content: Column(
              children: [
                Lottie.asset(
                  'assets/animations/banana.json',
                  height: 250,
                ),
                const SizedBox(height: 25),
                Text('$e'),
                const SizedBox(height: 25),
              ],
            ),
            backgroundColor: Colors.red[700],
          ),
        );
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return isVerified
        ? Home()
        : Scaffold(
            body: Padding(
            padding: const EdgeInsets.all(48.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Lottie.asset(
                  'assets/animations/email.json',
                  height: 250,
                  repeat: false,
                ),
                const SizedBox(height: 25),
                Text(
                  'Hemos mandado un mensaje de verificación a ${FirebaseAuth.instance.currentUser!.email}. Por favor, revisa tu bandeja de entrada y sigue las instrucciones.',
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                    fontSize: 20,
                    color: Colors.black,
                  ),
                ),
                const SizedBox(height: 25),
                ElevatedButton(
                  onPressed: canResend ? sendVerificationEmail : null,
                  child: const Text('Reenviar correo de verificación'),
                ),
              ],
            ),
          ));
  }
}
