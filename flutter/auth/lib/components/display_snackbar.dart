import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

void displaySnackbar(
    BuildContext context, Color color, Future future, String animationPath) {
  FocusScope.of(context).unfocus();

  showDialog(
    context: context,
    barrierDismissible: false, // Prevents closing the dialog by tapping outside
    builder: (context) {
      return FutureBuilder(
        future: future,
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
                          animationPath,
                          height: 250,
                        ),
                        const SizedBox(height: 25),
                        Text('${snapshot.error}'),
                        const SizedBox(height: 25),
                      ],
                    ),
                    backgroundColor: color,
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
