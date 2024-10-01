import 'package:auth/screens/login/loginpage.dart';
import 'package:auth/screens/login/register.dart';
import 'package:flutter/material.dart';

class LoginOrRegister extends StatefulWidget {
  const LoginOrRegister({super.key});

  @override
  State<LoginOrRegister> createState() => _LoginOrRegisterState();
}

class _LoginOrRegisterState extends State<LoginOrRegister> {
  bool login = true;

  void togglePages() {
    setState(() {
      login = !login;
    });
  }

  @override
  Widget build(BuildContext context) {
    return login
        ? Loginpage(
            toggle: togglePages,
          )
        : RegisterPage(toggle: togglePages);
  }
}
