import 'package:auth/screens/login/authpage.dart';
import 'package:auth/screens/login/reset_password.dart';
import 'package:auth/themes/theme.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:auth/screens/home.dart';
import 'package:auth/screens/intro/orboarding.dart';
import 'firebase_options.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: darkTheme,
      home: const Authpage(),
      routes: {
        '/onboarding': (context) => const OnBoardingScreen(),
        '/reset': (context) => const ResetPassword(),
        '/home': (context) => Home(),
        '/auth': (context) => const Authpage(),
      },
    );
  }
}
