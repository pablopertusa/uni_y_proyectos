import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:lottie/lottie.dart';
import 'package:auth/components/my_singin_button.dart';
import 'package:auth/components/my_textfield.dart';
import 'package:auth/components/squre_tile.dart';

class RegisterPage extends StatefulWidget {
  final void Function() toggle;
  const RegisterPage({super.key, required this.toggle});

  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  final userNameController = TextEditingController();
  final passwordController = TextEditingController();

  Future<void> googleSignIn() async {
    // Implement Google Sign-In
    try {
      final GoogleSignInAccount? googleUser = await GoogleSignIn().signIn();

      if (googleUser == null) {
        return;
      } else {
        final GoogleSignInAuthentication googleAuth =
            await googleUser.authentication;

        final AuthCredential googleAuthCredential =
            GoogleAuthProvider.credential(
          accessToken: googleAuth.accessToken,
          idToken: googleAuth.idToken,
        );

        await FirebaseAuth.instance.signInWithCredential(googleAuthCredential);
      }
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
                  'assets/animations/not_found.json',
                  height: 250,
                ),
                const SizedBox(height: 25),
                Text(e.toString()),
                const SizedBox(height: 25),
              ],
            ),
            backgroundColor: Colors.red,
          ),
        );
      });
    }
  }

  bool isValidEmail(String email) {
    final emailRegex = RegExp(r'^[^@]+@[^@]+\.[^@]+');
    return emailRegex.hasMatch(email);
  }

  Future<void> checkFieldsAndRegister() async {
    if (userNameController.text.isEmpty) {
      throw Exception('El campo de usuario está vacío.');
    }

    if (!isValidEmail(userNameController.text)) {
      throw Exception(
          'El campo de usuario no es un correo electrónico válido.');
    }
    if (passwordController.text.isEmpty) {
      throw Exception('El campo de contraseña está vacío.');
    }

    await FirebaseAuth.instance.createUserWithEmailAndPassword(
      email: userNameController.text.trim(),
      password: passwordController.text.trim(),
    );
  }

  void register() {
    // Close the keyboard
    FocusScope.of(context).unfocus();

    showDialog(
      context: context,
      barrierDismissible:
          false, // Prevents closing the dialog by tapping outside
      builder: (context) {
        return FutureBuilder(
          future: checkFieldsAndRegister(),
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
                // Close the dialog when the sign-in process is complete
                Navigator.of(context).pop();
                // After this, the user will navigate to the email verification page
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
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[300],
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const SizedBox(
                height: 50,
              ),
              Lottie.asset('assets/animations/register.json',
                  height: 175, fit: BoxFit.cover),
              const SizedBox(
                height: 25,
              ),
              Text(
                '¡Vamos a crear una cuenta!',
                style: TextStyle(
                    color: Colors.grey[800],
                    fontSize: 22,
                    fontWeight: FontWeight.bold),
              ),
              const SizedBox(
                height: 25,
              ),
              MyTextfield(
                controller: userNameController,
                hintText: 'Usuario',
                obscureText: false,
              ),
              const SizedBox(
                height: 15,
              ),
              MyTextfield(
                controller: passwordController,
                hintText: 'Contraseña',
                obscureText: true,
              ),
              const SizedBox(
                height: 25,
              ),
              MySinginButton(
                text: 'Registrar',
                onTap: register,
              ),
              const SizedBox(
                height: 25,
              ),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 25),
                child: Row(
                  children: [
                    Expanded(
                        child: Divider(
                      thickness: 1,
                      color: Colors.grey[500],
                    )),
                    Text(
                      'O continúa con',
                      style: TextStyle(color: Colors.grey[700]),
                    ),
                    Expanded(
                        child: Divider(
                      thickness: 1,
                      color: Colors.grey[500],
                    )),
                  ],
                ),
              ),
              const SizedBox(
                height: 50,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  GestureDetector(
                    onTap: googleSignIn,
                    child:
                        const SqureTile(imagePath: 'assets/images/google.png'),
                  ),
                  const SizedBox(
                    width: 20,
                  ),
                  GestureDetector(
                    child: const SqureTile(
                        imagePath: 'assets/images/facebook.png'),
                    onTap: () {
                      // Implement Facebook Sign-In
                    },
                  ),
                ],
              ),
              const SizedBox(
                height: 35,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    '¿Ya tienes una cuenta?',
                    style: TextStyle(color: Colors.grey[800], fontSize: 15),
                  ),
                  const SizedBox(
                    width: 5,
                  ),
                  GestureDetector(
                    onTap: widget.toggle,
                    child: const Text(
                      'Inicia sesión',
                      style: TextStyle(
                          color: Colors.blue,
                          fontWeight: FontWeight.bold,
                          fontSize: 17),
                    ),
                  ),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
