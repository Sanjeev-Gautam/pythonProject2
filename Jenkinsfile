pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/Sanjeev-Gautam/pythonProject2.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                sh 'python main.py'
            }
        }
    }
}