pipeline {
    agent any
    echo 'Pipeline shtarted!'

    environment {
        EC2_HOST = 'ec2-16-171-153-194.eu-north-1.compute.amazonaws.com'
        EC2_USER = 'ec2-user'
        EC2_SSH_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAyjwF9NJ39hoHvF0c+8xSMRAlr88tYePEmgmukBIm+r3xtgRs
QRwrr47QIjAIJpD9U9TAOP1UYZwLkRcKxI2D9etDzN4zDy0NWVLXkhs8ij5sxJGI
hiAtNVZMrr/EEQCkr9rIrGY/+smc1S/AYEIJhafkISrL4xhSrV+2umzTiAGUh7iF
8LRtctjPi4fnUJbtyJvTyiXUbV0exquzovMPLJWTlWdG5WTEMC3pWfplL2MZWu8u
cCMyUeyG32tyav1riWq+O8NYRaHiFN9isZiBrokTBxXg1aQkWDYQj8obIBLCafis
REGrHrKYgxrxOVRwVRznxTRDtpwZGMExh8f3xQIDAQABAoIBAQC2/csR9aPwvysC
yWpheUdh989yHtBcxEFwdJRM7u/wcREW9zeRTtFEwMAaP0YQx59CTL9GkgvZat6Y
gbYPllGyoxgtd13SPJzYl3pSTWzhVo0K7PkRDGp72cP3V7QtAl0CdsCgJsF7xxSv
Xs7/CqIdG4b0cAofSjH9iR8J31EkvVVX4W9r/EtHpA6IBQfllKFmWx5XjDyHwjsm
VaMRRDWiL47drvVYLKAituG3wluUHQ4Qpn9mm7mrhvEMCTGo7CEwVl+3v+6KecRE
0p3uf0G35gQDIgoYV2jf4kOU7WAI8NE+yHUp7X0uqajBmZU3i3rEUF6I46xGwZBX
9Va7vZSdAoGBAOp7ECcwvI+i1YSzBHuSZCts7IOTZYR4NgBNKxbdIelrwro7aR+T
B9tf449xUS/lKcQt+pPxyFTJueoSjQv0NjvdxTvQznUcQ9m91Mxh5NmoxAwHKWLI
7RGEvXaG5Su7Wwpy7oiqedJSLnl2bC/kGvqnNzG7KvOkKe5vz9SSIY4nAoGBANzL
XD5Zam/598qO798zo42ExF9to4xQJHOZKfTSZB5oin4EPuu615Qsgl2/h1X51cqf
wzi4/d0o4GkqS5uQ/vGOWoCFqa4rTea1VlIU0DZLv6qDNOU7Y05roESqgirmvr7u
ExaeMa9u4cah/elpN7SluGwqkW4bi/tL24vqL+ozAoGAewGL+8MpaAB4GmD/HQQy
4EUH3g5Y1yFo0seorxnaTGVnheLcxt+O45pt+jXr7UA+pNep+CqCeVhJ221X6Ml4
GffBHBvx8qWdQoC/PWitcTGDhvvKzjOxidskuSUS29oxbE3WrIMh3R+XmchyAL2d
GZjW75PMeHvKM3ccg9sVF0kCgYB5Myx8kUrLEvVBfLsR09/YxGOjWqTnVerchdwx
JviMdKhpSl1buyGxlckuOv/IYy9HXfGlBm9cYp7lO7FrQOmhoZnuaPDeyaimly4+
OmydEXGx4Po9Rx9ZId1FNC/l6uoUFs3loYr2mTBYf/3IjdhlUn7s6WURgw+RL2/h
2vjYXwKBgGuHEYYZb6tNJ9yLkEzlOD7i3Ex6O63zXzSALiAxafVvB1yRjwpaAniR
RKIn5KFyykqy9WkUJi60uq25K5moe2mGw4ofU8GfqbeJtsxLhBThfjsj7cd5AHdB
3FVbVAtGFOrWX/gOUvZNsEdcg0VdmkdU9bqG2w+wixOY3WJw9L3O
-----END RSA PRIVATE KEY-----'''
    }


    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git 'https://github.com/UkoHegdu/mikro'
            }
        }
        stage('Build') {
            steps {
                // Build your application
                sh 'mvn clean package'
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
