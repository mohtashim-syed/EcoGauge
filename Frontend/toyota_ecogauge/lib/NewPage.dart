import 'package:flutter/material.dart';

class NewPage extends StatelessWidget {
  final String query;

  const NewPage({Key? key, required this.query}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          // Red Header with Logo
          Container(
            color: const Color(0xFFEB0A1E), // Toyota red
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Image.asset(
                  'assets/images/image2.png', // Replace with your logo path
                  height: 40,
                ),
                const Spacer(), // Pushes the logo to the left
              ],
            ),
          ),

          // White Curved Section
          Expanded(
            child: Container(
              decoration: const BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(24),
                  topRight: Radius.circular(24),
                ),
              ),
              padding: const EdgeInsets.all(16),
              child: SingleChildScrollView(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Back Button and Title
                    Row(
                      children: [
                        IconButton(
                          icon: const Icon(Icons.arrow_back),
                          onPressed: () => Navigator.pop(context),
                        ),
                        const Text(
                          'Results',
                          style: TextStyle(
                            fontSize: 20,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 16),

                    // Query Text
                    Text(
                      'You searched for: "$query"',
                      style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 24),

                    // Dropdown for Chat Selection
                    // DropdownButtonFormField<String>(
                    //   decoration: InputDecoration(
                    //     labelText: "Choose Chatbot",
                    //     border: OutlineInputBorder(
                    //       borderRadius: BorderRadius.circular(8),
                    //     ),
                    //     contentPadding: const EdgeInsets.symmetric(horizontal: 16),
                    //   ),
                    //   items: const [
                    //     DropdownMenuItem(
                    //       value: "Miles",
                    //       child: Text("Miles (4.0-mini)"),
                    //     ),
                    //     DropdownMenuItem(
                    //       value: "Finn",
                    //       child: Text("Finn (3.5)"),
                    //     ),
                    //   ],
                    //   onChanged: (value) {
                    //     // Handle dropdown selection if needed
                    //     print("Selected Chatbot: $value");
                    //   },
                    //   hint: const Text("Select Chatbot"),
                    // ),
                    const SizedBox(height: 24),

                    // Placeholder for LLM Prompt
                    Container(
                      width: double.infinity,
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: const Color(0xFFE0E0E0),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: const Text(
                        '[Repeat LLM Prompt Here]',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                    const SizedBox(height: 24),

                    // Placeholder for Data Analysis
                    Container(
                      width: double.infinity,
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: const Color(0xFFE0E0E0),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: const Text(
                        '[Insert Data Analysis Here]\n[GPT Analysis]',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}