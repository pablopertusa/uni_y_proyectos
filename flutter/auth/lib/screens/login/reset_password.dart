import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ResetPassword extends StatefulWidget {
  const ResetPassword({super.key});

  @override
  State<ResetPassword> createState() => _ResetPasswordState();
}

class _ResetPasswordState extends State<ResetPassword> {
  final emailController = TextEditingController();

  Future<void> sendPasswordResetEmail(String email) async {
    final prefs = await SharedPreferences.getInstance();
    final lastResetTimestamp = prefs.getInt('lastPasswordReset') ?? 0;
    final currentTimestamp = DateTime.now().millisecondsSinceEpoch;

    // Check if 24 hours have passed since the last email
    if (currentTimestamp - lastResetTimestamp < 0.3 * 60 * 60 * 1000) {
      throw Exception(
          'Password reset email already sent within the last 30 minutes.');
    }

    // Send the password reset email
    await FirebaseAuth.instance.sendPasswordResetEmail(email: email);

    // Store the current timestamp in Shared Preferences
    await prefs.setInt('lastPasswordReset', currentTimestamp);
  }

  void resetPassword() async {
    FocusScope.of(context).unfocus();

    showDialog(
      context: context,
      barrierDismissible:
          false, // Prevents closing the dialog by tapping outside
      builder: (context) {
        return FutureBuilder(
          future: sendPasswordResetEmail(emailController.text.trim()),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.done) {
              if (snapshot.hasError) {
                // Show error in a SnackBar
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
                          Text('${snapshot.error}'),
                          const SizedBox(height: 25),
                        ],
                      ),
                      backgroundColor: Colors.red[700],
                    ),
                  );
                });
                // Close the dialog
                Navigator.of(context).pop();
              } else {
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
                            'assets/animations/email.json',
                            height: 250,
                          ),
                          const SizedBox(height: 25),
                          const Text(
                              'Se ha enviado un correo electrónico para restablecer su contraseña'),
                          const SizedBox(height: 25),
                        ],
                      ),
                      backgroundColor: Colors.blue[700],
                    ),
                  );
                });
                // Close the dialog when the sign-in process is complete
                Navigator.of(context).pop();
              }
            }
            return Center(
              child: CircularProgressIndicator(
                valueColor: const AlwaysStoppedAnimation<Color>(
                    Colors.yellow), // Custom color
                backgroundColor: Colors.grey[500], // Custom background color
                strokeWidth: 6.0, // Custom stroke width
              ),
            );
          },
        );
      },
    );
  }

  @override
  void dispose() {
    emailController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
                'Introduzca su correo electrónico para restablecer su contraseña'),
            const SizedBox(
              height: 20,
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: TextField(
                controller: emailController,
                decoration: const InputDecoration(
                  hintText: 'Correo electrónico',
                ),
              ),
            ),
            ElevatedButton(
              onPressed: resetPassword,
              child: const Text('Enviar email'),
            ),
            TextButton(
                onPressed: () {
                  Navigator.of(context).pushNamed('/auth');
                },
                child: const Text('Volver')),
          ],
        ),
      ),
    );
  }
}
