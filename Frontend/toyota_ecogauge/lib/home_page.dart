// written and tweaked by Hammad and Mohtashim
import 'package:flutter/material.dart';
import 'simple_line_graph.dart'; // Import the graph widget
import 'NewPage.dart'; // Import the new page for navigation

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final screenHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      body: Column(
        children: [
          // Red Header with Logo
          Container(
            color: const Color(0xFFEB0A1E), // Toyota red
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
            child: Row(
              children: [
                Image.asset(
                  'assets/images/image2.png', // Path to the image
                  height: 40,
                ),
                const Spacer(),
              ],
            ),
          ),

          // White Section with Curves
          Expanded(
            child: Container(
              decoration: const BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(24),
                  topRight: Radius.circular(24),
                ),
              ),
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: SingleChildScrollView(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      // Greeting Text
                      const Text(
                        "Hello Koji Sato, how can we assist you in exploring the data today?",
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          fontFamily: 'Roboto', // Set Roboto font
                        ),
                      ),
                      const SizedBox(height: 16),

                      // Dropdown for Chat Selection
                      DropdownButtonFormField<String>(
                        decoration: InputDecoration(
                          labelText: "Choose Chatbot",
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                          ),
                          contentPadding:
                              const EdgeInsets.symmetric(horizontal: 16),
                        ),
                        items: const [
                          DropdownMenuItem(
                            value: "Miles",
                            child: Text("Chat with Miles (4.0-mini)"),
                          ),
                          DropdownMenuItem(
                            value: "Finn",
                            child: Text("Chat with Finn (3.5)"),
                          ),
                        ],
                        onChanged: (value) {
                          // Handle dropdown selection if needed
                          print("Selected Chatbot: $value");
                        },
                        hint: const Text("Select Chatbot"),
                      ),
                      const SizedBox(height: 24),

                      // Chat Input Box
                      TextField(
                        decoration: InputDecoration(
                          hintText: "Discover Insights. Ask away",
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(8),
                          ),
                          contentPadding:
                              const EdgeInsets.symmetric(horizontal: 16),
                        ),
                        onSubmitted: (query) {
                          // Navigate to NewPage with the query
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => NewPage(query: query),
                            ),
                          );
                        },
                      ),
                      const SizedBox(height: 24),

                      // Graph Area with the SimpleLineGraph Widget
                      Container(
                        height: 350, // Height for the graph
                        decoration: BoxDecoration(
                          border: Border.all(color: Colors.grey.shade300),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: SimpleLineGraph(), // Restored SimpleLineGraph widget
                      ),
                      const SizedBox(height: 24),

                      // Dropdown for Toyota Models and Trim
                      Row(
                        children: [
                          Expanded(
                            child: DropdownButtonFormField<String>(
                              decoration: InputDecoration(
                                labelText: "Model",
                                border: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                contentPadding:
                                    const EdgeInsets.symmetric(horizontal: 16),
                              ),
                              items: const [
                                DropdownMenuItem(
                                  value: "Corolla",
                                  child: Text("Corolla"),
                                ),
                                DropdownMenuItem(
                                  value: "Camry",
                                  child: Text("Camry"),
                                ),
                                DropdownMenuItem(
                                  value: "RAV4",
                                  child: Text("RAV4"),
                                ),
                                DropdownMenuItem(
                                  value: "Prius",
                                  child: Text("Prius"),
                                ),
                              ],
                              onChanged: (value) {
                                // Handle model selection
                              },
                              hint: const Text("Select Model"),
                            ),
                          ),
                          const SizedBox(width: 16),
                          Expanded(
                            child: DropdownButtonFormField<String>(
                              decoration: InputDecoration(
                                labelText: "Trim",
                                border: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                contentPadding:
                                    const EdgeInsets.symmetric(horizontal: 16),
                              ),
                              items: const [
                                DropdownMenuItem(
                                  value: "Base",
                                  child: Text("Base"),
                                ),
                                DropdownMenuItem(
                                  value: "Sport",
                                  child: Text("Sport"),
                                ),
                                DropdownMenuItem(
                                  value: "Hybrid",
                                  child: Text("Hybrid"),
                                ),
                                DropdownMenuItem(
                                  value: "Limited",
                                  child: Text("Limited"),
                                ),
                              ],
                              onChanged: (value) {
                                // Handle trim selection
                              },
                              hint: const Text("Select Trim"),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 24),

                      // Tabular View with Alternating Colors (Centered Vertically)
                      Center(
                        child: SingleChildScrollView(
                          scrollDirection: Axis.horizontal,
                          child: DataTable(
                            headingRowColor: MaterialStateProperty.resolveWith(
                              (states) => const Color(0xFFEB0A1E), // Header background
                            ),
                            headingTextStyle: const TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                              fontFamily: 'Roboto', // Use Roboto font
                            ),
                            columns: const [
                              DataColumn(
                                label: Center(
                                  child: Text(
                                    "Year",
                                    style: TextStyle(fontFamily: 'Roboto'),
                                  ),
                                ),
                              ),
                              DataColumn(
                                label: Center(
                                  child: Text(
                                    "City MPG",
                                    style: TextStyle(fontFamily: 'Roboto'),
                                  ),
                                ),
                              ),
                              DataColumn(
                                label: Center(
                                  child: Text(
                                    "Highway MPG",
                                    style: TextStyle(fontFamily: 'Roboto'),
                                  ),
                                ),
                              ),
                            ],
                            rows: List<DataRow>.generate(
                              5,
                              (index) {
                                // Alternating row colors: light red for even, white for odd
                                final color = index % 2 == 0
                                    ? const Color(0xFFFFE6E6) // Light red
                                    : Colors.white; // White
                                return DataRow(
                                  color: MaterialStateProperty.resolveWith(
                                    (states) => color,
                                  ),
                                  cells: [
                                    DataCell(
                                      Center(
                                        child: Text(
                                          "${2021 + index}",
                                          style: const TextStyle(
                                              fontFamily: 'Roboto'),
                                        ),
                                      ),
                                    ),
                                    DataCell(
                                      Center(
                                        child: Text(
                                          "${30 + index}",
                                          style: const TextStyle(
                                              fontFamily: 'Roboto'),
                                        ),
                                      ),
                                    ), // City MPG
                                    DataCell(
                                      Center(
                                        child: Text(
                                          "${38 + index}",
                                          style: const TextStyle(
                                              fontFamily: 'Roboto'),
                                        ),
                                      ),
                                    ), // Highway MPG
                                  ],
                                );
                              },
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
