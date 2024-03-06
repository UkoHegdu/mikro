pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile sources/server_side_rend.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}