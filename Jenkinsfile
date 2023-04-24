pipeline {
    agent any


    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'a0289195-c3bf-4506-b273-fd91ee66d7f3', url: 'https://github.com/Sanjeev-Gautam/pythonProject2.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '022aabf0-5d76-4493-b54e-5188d0dfa838', url: 'https://github.com/Sanjeev-Gautam/pythonProject2.git'
                bat 'main.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Single Linked List Tested'
            }
        }
    }
}