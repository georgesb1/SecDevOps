import spacy
nlp = spacy.load("en_core_web_sm")

def handle_user_message(user_message):
    bot_reply = ""
    doc = nlp(user_message)

    qa_pairs = {
        "newer versions": "Yes, there's a newer version of the software available. You can download it from our website.",
        "quantum mechanical calculation": "Our software uses advanced quantum algorithms and parallel processing to perform complex quantum mechanical calculations efficiently.",
        "creator of this software": "Our software was created by @induction to perform complex quantum mechanical calculations like Quantum Chromodynamics (QCD, Nuclear Structure, Quantum Many-Body Theory, Molecular Structure and Bonding, and many more.",
        "software crashing": "I'm sorry to hear that you're experiencing crashes. To resolve this issue, please try the following steps:\n1. Update the software to the latest version.\n2. Check your system's hardware requirements.\n3. Verify that you have enough memory and disk space.\n4. Disable any conflicting software or extensions.\n5. Contact our support team for further assistance.",
        "version control": "We use Git for version control. All code is stored in repositories, and we follow branching strategies to manage feature development, bug fixes, and releases.",
        "continuous integration and continuous deployment": "We have implemented Jenkins for continuous integration and continuous deployment. Code changes are automatically built, tested, and deployed to various environments.",
        "automated testing": "We use a combination of unit tests, integration tests, and end-to-end tests. Testing frameworks like JUnit and Selenium are utilized for automated testing to maintain code quality and reliability.",
        "dependency management": "We employ package managers like Maven for Java-based dependencies and npm for JavaScript dependencies. Regular security scans and updates are part of our process.",
        "code review": "Code reviews are mandatory for all changes. We use tools like GitHub's pull requests for peer reviews to ensure code quality and collaboration.",
        "monitoring and logging": "We utilize Prometheus for monitoring and ELK stack for log management. Alerts are set up to notify us of any performance or operational issues.",
        "backup and disaster recovery": "Regular backups are taken and stored in geographically distributed locations. We have a documented disaster recovery plan that is periodically tested.",
        "resource scaling": "Auto-scaling is implemented in our cloud infrastructure to handle variable workloads efficiently.",
        "security measures": "Security is a top priority. We perform regular security audits, use WAFs, encryption, and access controls. Compliance with regulations is ensured.",
        "release process": "Releases are done using a blue-green deployment strategy to minimize downtime. Feature flags are used to enable/disable new features for users.",
        "configuration management": "Infrastructure as code (IaC) is managed with tools like Terraform and Ansible. Configuration changes are tracked and versioned.",
        "knowledge sharing": "We maintain documentation in a knowledge base and use collaboration tools like Confluence to share information within the DevOps team.",
        "continuous improvement": "We conduct retrospectives after each release to identify areas of improvement. Feedback is incorporated into our DevOps processes.",
        "API versioning": "We maintain backward compatibility for APIs, and versioning is done using API version numbers in the URL.",
        "DevOps collaboration": "We use tools like Slack and integrate them with our CI/CD pipelines to ensure real-time communication between development and operations teams."
    }

    for question, answer in qa_pairs.items():
        if question in user_message:
            bot_reply = answer
            break

    if not bot_reply:
        bot_reply = "I didn't quite catch that. Could you please rephrase your question, or ask something else?"

    return bot_reply
