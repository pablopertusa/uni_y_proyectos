import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class VerificacionScreen extends StatefulWidget {
  const VerificacionScreen({super.key});

  @override
  State<VerificacionScreen> createState() => _VerificacionScreenState();
}

class _VerificacionScreenState extends State<VerificacionScreen> {
  @override
  void initState() {
    super.initState();
    sendVerification();
  }

  void sendVerification() {
    // Your code here
    FirebaseAuth.instance.currentUser!.sendEmailVerification();
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Center(
        child: Column(
          children: [
            const Center(child: Text('VerificacionScreen')),
            ElevatedButton(
              onPressed: () {
                FirebaseAuth.instance.currentUser!.sendEmailVerification();
              },
              child: const Text('Reenviar correo de verificacion'),
            ),
          ],
        ),
      ),
    );
  }
}
