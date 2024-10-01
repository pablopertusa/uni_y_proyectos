import 'package:flutter/material.dart';
import 'package:auth/screens/intro/page1.dart';
import 'package:auth/screens/intro/page2.dart';
import 'package:auth/screens/intro/page3.dart';
import 'package:smooth_page_indicator/smooth_page_indicator.dart';

class OnBoardingScreen extends StatefulWidget {
  const OnBoardingScreen({super.key});

  @override
  State<OnBoardingScreen> createState() => _OnBoardingScreenState();
}

class _OnBoardingScreenState extends State<OnBoardingScreen> {
  final PageController _controller = PageController();
  bool onLastPage = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          PageView(
            onPageChanged: (int page) {
              if (page == 2) {
                setState(() {
                  onLastPage = true;
                });
              } else {
                setState(() {
                  onLastPage = false;
                });
              }
            },
            controller: _controller,
            children: const [Page1(), Page2(), Page3()],
          ),
          Container(
            alignment: const Alignment(0, 0.85),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                GestureDetector(
                  onTap: () {
                    _controller.jumpToPage(2);
                  },
                  child: const Text(
                    'Saltar',
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 18,
                        fontWeight: FontWeight.bold),
                  ),
                ),
                SmoothPageIndicator(
                  controller: _controller,
                  count: 3,
                  effect: const WormEffect(
                      dotColor: Colors.black45,
                      activeDotColor: Colors.white,
                      dotHeight: 10,
                      dotWidth: 30),
                ),
                onLastPage
                    ? GestureDetector(
                        onTap: () {
                          Navigator.pushReplacementNamed(context, '/auth');
                        },
                        child: const Text('Hecho',
                            style: TextStyle(
                                color: Colors.white,
                                fontSize: 18,
                                fontWeight: FontWeight.bold)),
                      )
                    : GestureDetector(
                        onTap: () {
                          _controller.nextPage(
                              duration: const Duration(milliseconds: 400),
                              curve: Curves.easeIn);
                        },
                        child: const Text('Siguiente',
                            style: TextStyle(
                                color: Colors.white,
                                fontSize: 18,
                                fontWeight: FontWeight.bold)),
                      ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
