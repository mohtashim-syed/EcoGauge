import 'package:flutter/material.dart';
import 'splash_screen.dart'; // Import your SplashScreen file
import 'login_page.dart'; // Import your LoginPage file
import 'home_page.dart'; // Import your HomePage file

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Toyota Employee Dashboard',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.red),
        useMaterial3: true,
      ),
      home: const SplashScreen(), // Set SplashScreen as the initial screen
    );
  }
}