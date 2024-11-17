import 'dart:async';
import 'package:flutter/material.dart';
import 'login_page.dart'; // Import LoginPage

class SplashScreen extends StatelessWidget {
  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // Navigate to LoginPage after 3 seconds
    Timer(Duration(seconds: 3), () {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) => const LoginPage(), // Navigate to LoginPage
        ),
      );
    });

    return Scaffold(
      body: Container(
        width: double.infinity, // Full width
        height: double.infinity, // Full height
        color: Colors.white, // White background
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Image.asset(
                'assets/images/image.png', // Replace with the correct image path
                height: 170,
                width: 166,
              ),
              const SizedBox(height: 20),
            ],
          ),
        ),
      ),
    );
  }
}