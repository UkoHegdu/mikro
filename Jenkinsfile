pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile sources/server_side_rend.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
        stage('Deploy')  { 
            steps { 
                echo "deploying the application"
                sh "sudo nohup python3 app.py > log.txt 2>&1 &"
            } 
        } 
    }
}