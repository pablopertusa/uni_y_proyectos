import 'package:auth/screens/pages/camera.dart';
import 'package:auth/themes/theme.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  void userSignOut() async {
    FirebaseAuth.instance.signOut();
  }

  final User user = FirebaseAuth.instance.currentUser!;
  int _index = 0;

  bool checkIndex(int index, int selectedIndex) {
    return index == selectedIndex;
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        backgroundColor: darkTheme.colorScheme.surface,
        floatingActionButton: SizedBox(
          height: 70,
          width: 70,
          child: FloatingActionButton(
            elevation: 10,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const Camera(),
                ),
              );
            },
            child: const Icon(
              size: 30,
              Icons.camera_alt,
            ),
          ),
        ),
        resizeToAvoidBottomInset: false,
        drawer: Drawer(
          child: Column(
            children: [
              UserAccountsDrawerHeader(
                accountName: const Text('pablo'),
                accountEmail: const Text('email'),
                currentAccountPicture: Image.asset('assets/images/apple.png'),
              ),
              const ListTile(
                title: Text('Opciones'),
                leading: Text('data'),
              )
            ],
          ),
        ),
        extendBodyBehindAppBar: true,
        bottomNavigationBar: NavigationBar(
            height: 60,
            indicatorColor: Colors.transparent,
            overlayColor: const WidgetStatePropertyAll(Colors.transparent),
            destinations: [
              NavigationDestination(
                icon: Icon(
                  color:
                      checkIndex(0, _index) ? Colors.white : Colors.grey[700],
                  Icons.home,
                  size: 35,
                ),
                label: 'Home',
              ),
              NavigationDestination(
                icon: Icon(
                  color: checkIndex(1, _index) ? Colors.white : Colors.grey,
                  Icons.search,
                  size: 35,
                ),
                label: 'Calendar',
              ),
            ],
            labelBehavior: NavigationDestinationLabelBehavior.alwaysHide,
            selectedIndex: _index,
            onDestinationSelected: (int index) {
              setState(() {
                _index = index;
              });
            }),
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
          actions: [
            IconButton(
              onPressed: userSignOut,
              icon: const Icon(
                Icons.logout,
              ),
            )
          ],
        ),
        body: [
          Container(
            child: const Center(
              child: Icon(Icons.home, size: 100, color: Colors.black),
            ),
          ),
          Container(
            child: const Center(
              child: Icon(Icons.search_rounded, size: 100, color: Colors.black),
            ),
          ),
        ][_index],
      ),
    );
  }
}
