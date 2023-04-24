pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']], // The branch to checkout
                    userRemoteConfigs: [[url: 'https://github.com/Sanjeev-Gautam/pythonProject2.git']], // The GitHub repository URL
                    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'my_project']] // The directory to checkout to
                ])
            }
        }

        stage('Build') {
            steps {
                sh 'main.py' // Run tests
            }
        }
    }
}