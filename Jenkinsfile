
pipeline {
    agent any
    

    environment {
        EC2_HOST = 'ec2-16-171-153-194.eu-north-1.compute.amazonaws.com'
        EC2_USER = 'ec2-user'
        EC2_SSH_KEY = '/atsleegas/webserver_key_copy.pem'
    }


    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout ipeline shtarted!'
                // Checkout code from Git repository
                git 'https://github.com/UkoHegdu/mikro'
            }
        }
        stage('Build') { 
            steps {
                echo 'build shtarted!'
                sh 'python -m py_compile server_side_rend.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
        stage('Test') {
            steps {
                // Run tests
                echo 'running tests (not really)'
            }
        }
        stage('Setup') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                // Use SSH to deploy to EC2 instance
                sh "ssh -i ${EC2_SSH_KEY} ${EC2_USER}@${EC2_HOST} 'echo Hello, World!'"
            }
        }
    }

    // Post-build actions (optional)
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
