import 'package:flutter/material.dart';

class MyTextfield extends StatelessWidget {
  final bool obscureText;
  final String hintText;
  final TextEditingController controller;

  const MyTextfield({
    super.key,
    required this.obscureText,
    required this.hintText,
    required this.controller,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 25),
      child: TextField(
        style: const TextStyle(fontSize: 18),
        onTap: () {
          ScaffoldMessenger.of(context).hideCurrentSnackBar();
        },
        obscureText: obscureText,
        controller: controller,
        decoration: InputDecoration(
            focusedBorder: const OutlineInputBorder(
              borderSide: BorderSide(color: Colors.grey),
              borderRadius: BorderRadius.all(Radius.circular(4)),
            ),
            enabledBorder: const OutlineInputBorder(
              borderSide: BorderSide(color: Colors.white),
              borderRadius: BorderRadius.all(Radius.circular(4)),
            ),
            fillColor: Colors.white,
            filled: true,
            hintText: hintText,
            hintStyle: TextStyle(color: Colors.grey[500])),
      ),
    );
  }
}
