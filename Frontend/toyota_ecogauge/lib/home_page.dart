import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.red,
        title: Row(
          children: [
            Image.asset(
              'assets/images/image.png', // Toyota logo
              width: 40,
            ),
            const SizedBox(width: 10),
            const Text("TOYOTA"),
          ],
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "Hello Kiichiro, what data would you like to see today?",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 20),

            // Example data cards
            Expanded(
              child: ListView(
                children: [
                  Card(
                    elevation: 4,
                    child: ListTile(
                      leading: const Icon(Icons.local_gas_station, color: Colors.red),
                      title: const Text("Fuel Efficiency"),
                      subtitle: const Text("34 MPG (Average)"),
                      trailing: const Icon(Icons.arrow_forward_ios),
                      onTap: () {
                        // Navigate to detailed view
                      },
                    ),
                  ),
                  Card(
                    elevation: 4,
                    child: ListTile(
                      leading: const Icon(Icons.speed, color: Colors.red),
                      title: const Text("Mileage"),
                      subtitle: const Text("12,500 miles"),
                      trailing: const Icon(Icons.arrow_forward_ios),
                      onTap: () {
                        // Navigate to detailed view
                      },
                    ),
                  ),
                  Card(
                    elevation: 4,
                    child: ListTile(
                      leading: const Icon(Icons.build, color: Colors.red),
                      title: const Text("Engine Status"),
                      subtitle: const Text("No Issues Detected"),
                      trailing: const Icon(Icons.arrow_forward_ios),
                      onTap: () {
                        // Navigate to detailed view
                      },
                    ),
                  ),
                ],
              ),
            ),

            // Chatbot Button
            Align(
              alignment: Alignment.bottomCenter,
              child: FloatingActionButton.extended(
                backgroundColor: Colors.red,
                icon: const Icon(Icons.chat),
                label: const Text("Chat with Miles"),
                onPressed: () {
                  // Open chatbot
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
