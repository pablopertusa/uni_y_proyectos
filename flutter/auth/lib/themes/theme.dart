import 'package:flutter/material.dart';

final ThemeData darkTheme = ThemeData(
    brightness: Brightness.dark,
    colorScheme: colorScheme,
    scaffoldBackgroundColor: Colors.black,
    appBarTheme: const AppBarTheme(
      color: Colors.black,
      iconTheme: IconThemeData(color: Colors.white),
    ),
    buttonTheme: const ButtonThemeData(
      buttonColor: Colors.tealAccent,
      textTheme: ButtonTextTheme.primary,
    ),
    iconTheme: const IconThemeData(color: Colors.white),
    navigationBarTheme: const NavigationBarThemeData(
      backgroundColor: Colors.black,
      surfaceTintColor: Colors.grey,
      indicatorColor: Colors.white,
    ),
    floatingActionButtonTheme: const FloatingActionButtonThemeData(
      backgroundColor: Colors.black,
      foregroundColor: Colors.white,
    ),
    drawerTheme: const DrawerThemeData(
      backgroundColor: Colors.black,
    ));

final ColorScheme colorScheme = ColorScheme(
    brightness: Brightness.dark,
    primary: Colors.yellow,
    onPrimary: Colors.black,
    secondary: Colors.blue,
    onSecondary: Colors.white,
    error: Colors.red,
    onError: Colors.black,
    surface: Colors.grey[800]!,
    onSurface: Colors.white);
