import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter_facebook_auth/flutter_facebook_auth.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:lottie/lottie.dart';
import 'package:auth/components/my_singin_button.dart';
import 'package:auth/components/my_textfield.dart';
import 'package:auth/components/squre_tile.dart';

class Loginpage extends StatefulWidget {
  final void Function() toggle;
  const Loginpage({super.key, required this.toggle});

  @override
  State<Loginpage> createState() => _LoginpageState();
}

class _LoginpageState extends State<Loginpage> {
  final emailController = TextEditingController();

  final passwordController = TextEditingController();

  Future<void> facebookSignIn() async {
    // Implement Facebook Sign-In
    try {
      final facebookLoginResult = await FacebookAuth.instance.login();

      if (facebookLoginResult.status == LoginStatus.success) {
        final AuthCredential facebookAuthCredential =
            FacebookAuthProvider.credential(
          facebookLoginResult.accessToken!.tokenString,
        );

        await FirebaseAuth.instance
            .signInWithCredential(facebookAuthCredential);
      } else {
        print('me cago en la puta');
        throw Exception('Facebook Sign-In failed.');
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

  Future<void> checkFieldsAndSignIn(String email, String password) async {
    if (email.isEmpty) {
      throw Exception('Email field is empty.');
    }
    if (!isValidEmail(email)) {
      throw Exception(
          'El campo de usuario no es un correo electrónico válido.');
    }
    if (password.isEmpty) {
      throw Exception('Password field is empty.');
    }

    await FirebaseAuth.instance.signInWithEmailAndPassword(
      email: email,
      password: password,
    );
  }

  void signIn() async {
    FocusScope.of(context).unfocus();

    showDialog(
      context: context,
      barrierDismissible:
          false, // Prevents closing the dialog by tapping outside
      builder: (context) {
        return FutureBuilder(
          future: checkFieldsAndSignIn(
              emailController.text.trim(), passwordController.text.trim()),
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
              Lottie.asset('assets/animations/meals.json',
                  height: 200, fit: BoxFit.cover),
              const SizedBox(
                height: 40,
              ),
              Text(
                '¡Nos vemos de nuevo!',
                style: TextStyle(
                    color: Colors.grey[800],
                    fontSize: 22,
                    fontWeight: FontWeight.bold),
              ),
              const SizedBox(
                height: 25,
              ),
              MyTextfield(
                controller: emailController,
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
                height: 10,
              ),
              GestureDetector(
                onTap: () {
                  Navigator.of(context).pushNamed('/reset');
                },
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 26),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      Text(
                        '¿Has olvidado tu contraseña?',
                        style: TextStyle(color: Colors.grey[800]),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(
                height: 25,
              ),
              MySinginButton(
                text: 'Iniciar sesión',
                onTap: signIn,
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
                height: 35,
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
                    onTap: facebookSignIn,
                    child: const SqureTile(
                        imagePath: 'assets/images/facebook.png'),
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
                    '¿Aún no tienes una cuenta?',
                    style: TextStyle(color: Colors.grey[800], fontSize: 15),
                  ),
                  const SizedBox(
                    width: 5,
                  ),
                  GestureDetector(
                    onTap: widget.toggle,
                    child: const Text(
                      'Regístrate',
                      style: TextStyle(
                          color: Colors.blue,
                          fontWeight: FontWeight.bold,
                          fontSize: 17),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 10),
            ],
          ),
        ),
      ),
    );
  }
}
