import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xFFEB0A1E), // Toyota red color
        title: const Center(
          child: Text(
            "TOYOTA",
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 24,
            ),
          ),
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Greeting Text
            const Text(
              "Hello Kiichiro, what data would you like to see today?",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 16),

            // Input Text Box
            TextField(
              decoration: InputDecoration(
                hintText: "Enter specific data or search...",
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8),
                ),
                contentPadding: const EdgeInsets.symmetric(horizontal: 16),
              ),
            ),
            const SizedBox(height: 24),

            // Placeholder for Graph Area
            Expanded(
              flex: 3,
              child: Container(
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey.shade300),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Center(
                  child: Text(
                    "Graph will be displayed here",
                    style: TextStyle(
                      fontSize: 16,
                      color: Colors.grey,
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 16),

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
                      contentPadding: const EdgeInsets.symmetric(horizontal: 16),
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
                      contentPadding: const EdgeInsets.symmetric(horizontal: 16),
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

            // Tabular View with Alternating Colors
            Expanded(
              flex: 4,
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: DataTable(
                  headingRowColor: MaterialStateProperty.resolveWith(
                    (states) => const Color(0xFFEB0A1E), // Header background
                  ),
                  headingTextStyle: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                  ),
                  columns: const [
                    DataColumn(label: Text("Year")),
                    DataColumn(label: Text("City MPG")),
                    DataColumn(label: Text("Highway MPG")),
                    DataColumn(label: Text("Combined MPG")),
                  ],
                  rows: List<DataRow>.generate(
                    5,
                    (index) {
                      // Alternating row colors: light red for even, white for odd
                      final color = index % 2 == 0
                          ? const Color(0xFFFFE6E6) // Light red
                          : Colors.white;
                      return DataRow(
                        color: MaterialStateProperty.resolveWith(
                          (states) => color,
                        ),
                        cells: [
                          DataCell(Text("${2021 + index}")),
                          DataCell(Text("${30 + index}")),
                          DataCell(Text("${38 + index}")),
                          DataCell(Text("${34 + index}")),
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
    );
  }
}
