
# Partick Litter-Project 🌿

Welcome to the Partick Litter-Project, a Streamlit application designed to engage the community in keeping Partick clean and litter-free. This student project is part of an initiative to raise awareness about littering, promote recycling, and foster community participation in clean-up events.

## Features
- **Manifesto**: Actions to keep Partick tidy!
- **Chatbot**: Interact with the Partick Litter Pal, a friendly chatbot here to answer your questions about litter prevention, recycling options, and upcoming community events.
- **Free Poster**: An awesome free poster for you to print and share. 

## Project Roadmap

- **Interactive Maps**: View maps highlighting litter hotspots and clean-up event locations.
- **Event Calendar**: Stay updated with a calendar of upcoming litter-picking events and how you can join.
- **Educational Resources**: Learn about recycling, reducing waste, and the impact of litter on the environment.

## How to Run

To run this Streamlit application on your local machine, follow these steps:

1. Clone the repository:
```bash
   git clone https://github.com/rdubar/litter-project.git
 ```
2. Navigate to the project directory:
```bash
   cd litter-project
 ```
3. Install dependencies (ensure you have Python installed):
```bash
   pip install -r requirements.txt
 ```
4. Set up your Open AI api key for the Chatbot.
```bash
   mkdir -p .streamlit
   touch .streamtlit/secrets.toml
```
Make sure your `.streamtlit/secrets.toml` file contains the following:
```bash
   [openai]
   openai_api_key = [YOUR API KEY GOES HERE]
```
5. Run the application:
```bash
   streamlit run Home.py
 ```

## Contributing

Contributions to the Partick Litter-Project are welcome! Here's how you can contribute:

- **Report Bugs**: Use the Issues tab to report and track bugs.
- **Feature Requests**: Have ideas on how to improve the app? Submit them as feature requests under Issues.
- **Pull Requests**: Want to contribute directly to the codebase? Submit a pull request with your proposed changes.

For more information, please read the CONTRIBUTING.md file.

## License

- This project is licensed under the MIT License - see the LICENSE file for details.
- The project poster is licensed for non-commercial use under the [CC BY-NC 4.0 DEED License](https://creativecommons.org/licenses/by-nc/4.0/).

## Contact

If you have any questions, you can reach out by emailing [rdubar@gmail.com](mailto:rdubar@gmail.com).

Thank you for supporting our efforts to keep Partick clean!
