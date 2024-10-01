import 'package:auth/components/recipe.dart';
import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      physics: const NeverScrollableScrollPhysics(),
      child: ConstrainedBox(
        constraints: BoxConstraints(
          minWidth: MediaQuery.of(context).size.width,
          minHeight: MediaQuery.of(context).size.height,
        ),
        child: SafeArea(
            child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 10),
              child: SearchBar(
                hintText: 'Search for recipes',
                elevation: const WidgetStatePropertyAll(0),
                shape: WidgetStatePropertyAll(
                  RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                    side: const BorderSide(color: Colors.grey, width: 1.5),
                  ),
                ),
                leading: const Padding(
                  padding: EdgeInsets.all(12.0),
                  child: Icon(Icons.search),
                ),
              ),
            ),
            const SizedBox(height: 20),
            const Padding(
              padding: EdgeInsets.symmetric(horizontal: 25),
              child: SizedBox(
                width: double.infinity,
                child: Text(
                  'Discover new recipes',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                  textAlign: TextAlign.left,
                ),
              ),
            ),
            const SizedBox(height: 10),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 18),
              child: SizedBox(
                height: 200,
                child: CarouselView(
                  itemExtent: 200,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(24),
                  ),
                  children: const [
                    Recipe(
                      image: 'assets/images/recipe2.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe2.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe2.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe2.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 20),
            const Padding(
              padding: EdgeInsets.symmetric(horizontal: 25),
              child: SizedBox(
                width: double.infinity,
                child: Text(
                  'Saved recipes',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                  textAlign: TextAlign.left,
                ),
              ),
            ),
            const SizedBox(height: 10),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 18),
              child: SizedBox(
                height: 200,
                child: CarouselView(
                  itemExtent: 200,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(24),
                  ),
                  children: const [
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                    Recipe(
                      image: 'assets/images/recipe3.png',
                      time: '10 min',
                      recipeName: 'Recipe 1',
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(
              height: 30,
            ),
            Container(
              width: 350,
              height: 60,
              decoration: ShapeDecoration(
                color: const Color.fromRGBO(77, 85, 99, 1),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
              ),
              child: const Center(
                child: Text(
                  'Upload my recipe',
                  style: TextStyle(
                      color: Colors.white,
                      fontSize: 20,
                      fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        )),
      ),
    );
  }
}
