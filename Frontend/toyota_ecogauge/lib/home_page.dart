import 'package:flutter/material.dart';
import 'simple_line_graph.dart'; // Import the graph widget

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xFFEB0A1E), // Toyota red color
        title: Row(
          children: [
            Image.asset(
              'assets/images/image2.png', // Path to the image
              height: 40, // Adjust the height to fit within the banner
            ),
            const SizedBox(width: 10), // Space between image and text
            const Expanded(
              child: Center(
                child: Text(
                  "ECOGAUGE",
                  style: TextStyle(
                    fontFamily: 'Roboto', // Use the Roboto font
                    fontWeight: FontWeight.bold,
                    fontSize: 24,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16),
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

              // Input Text Box
              TextField(
                decoration: InputDecoration(
                  hintText: "Discover insights - Just ask Miles!",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(8),
                  ),
                  contentPadding: const EdgeInsets.symmetric(horizontal: 16),
                ),
              ),
              const SizedBox(height: 24),

              // Graph Area with the SimpleLineGraph Widget
              Container(
                height: 350, // Increased height for better spacing
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey.shade300),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: SimpleLineGraph(), // Integrated graph widget
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
                                  style: const TextStyle(fontFamily: 'Roboto'),
                                ),
                              ),
                            ),
                            DataCell(
                              Center(
                                child: Text(
                                  "${30 + index}",
                                  style: const TextStyle(fontFamily: 'Roboto'),
                                ),
                              ),
                            ), // City MPG
                            DataCell(
                              Center(
                                child: Text(
                                  "${38 + index}",
                                  style: const TextStyle(fontFamily: 'Roboto'),
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
    );
  }
}
