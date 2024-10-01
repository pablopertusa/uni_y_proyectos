import 'package:flutter/material.dart';

class Fab extends StatelessWidget {
  const Fab({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 70,
      width: 70,
      child: FloatingActionButton(
        elevation: 10,
        onPressed: () {},
        backgroundColor: Colors.black,
        child: const Icon(
          size: 30,
          Icons.camera_alt,
          color: Colors.white,
        ),
      ),
    );
  }
}
