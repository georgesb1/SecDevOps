pipeline {
    agent any 
    stages{
        stage("Checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git']])
            }
        }
        stage("CheckSecret"){
            steps{
                  sh 'rm trufflehog || true'
                sh 'docker run gesellix/trufflehog --json https://github.com/georgesb1/SecDevOps.git > trufflehog'
                sh 'cat trufflehog'
            }
        }
        
        stage("Source Composition Analysis"){
            steps{
               // sh ' rm Owasp* || true'
                //sh ' wget https://raw.githubusercontent.com/georgesb1/SecDevOps/main/Owasp-dependency-check.sh '
                //sh 'chmod +x Owasp-dependency-check.sh'
                //sh 'bash Owasp-dependency-check.sh'
                //sh 'cat /home/kali/OWASP-Dependency-Check/reports/dependency-check-report.xml'
            }
        }

       stage('SAST with SonarQube ') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('Sonarqube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage("Build") {
            steps {
                script {
                    def harborPassword = credentials('harbor')
                    sh "echo ${BUILD_NUMBER}"
                    sh "docker build -t chatbot:${BUILD_NUMBER} ."
                    // Use the credentials for Docker login
                    withCredentials([string(credentialsId: 'harbor', variable: 'HARBOR_PASSWORD')]) {
                        sh "docker login https://core.harbor.domain:30609/ -u admin -p ${HARBOR_PASSWORD}"
                    }
                   sh "docker tag chatbot:${BUILD_NUMBER} core.harbor.domain:30609/myregistry/chatbot:${BUILD_NUMBER}"
                   sh "docker push core.harbor.domain:30609/myregistry/chatbot:${BUILD_NUMBER}"
                }
            }
        }


        stage("DAST with OWASP ZAP"){
            steps{
                sh ' rm report.xml || true'
                sh ' echo yes '
            }
        }

        stage("Deploy on kubernetes"){
            steps{
                withKubeConfig(caCertificate: '''LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCakNDQWU2Z0F3SUJBZ0lCQVRBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwdGFXNXAKYTNWaVpVTkJNQjRYRFRJek1USXhOekV6TWpJeU5sb1hEVE16TVRJeE5URXpNakl5Tmxvd0ZURVRNQkVHQTFVRQpBeE1LYldsdWFXdDFZbVZEUVRDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBT2dpCmVhQ09pTzlQQUdyNjg0UVR4RXVzMGJydy8xTXVjYWlqL2t0WVFhVU5kcDArTEZyanNITzljZWN5VHMyZnZWQ28KM1hCQ1J4RlZRMkU0RC9WRFlRNGJYRk9EWXpMcTM5R01ZSlVkdXMxQko0MFlsU2dodEllaTg5TGVFWlpaM1VYagpObXg2YnNOWWNzSUQwRE1jQ3dqLytTQUNFSVVWYkdPM1lDNmJvM1d2NkNsejYzRU5CenlGN0hUc3lremFFWCtFCmF1K05ZSnZYUm5DUUd4cmdoTHY0Y092bFIxMC9nOEQyVW9MUlZTVDBHcHluWUp5TzkvZjFsbWMxL0JEZ2RqUDIKeHNMWUZsNXNuZHVMVHFZNU40OWw1MWpmMDV2L0d4UGZ3RDg5blN1REZldFQ1bG5vZXJCNDA5VkNPYUFHTDZHeApNZlp3M25WZEU1SkJTS0htamdNQ0F3RUFBYU5oTUY4d0RnWURWUjBQQVFIL0JBUURBZ0trTUIwR0ExVWRKUVFXCk1CUUdDQ3NHQVFVRkJ3TUNCZ2dyQmdFRkJRY0RBVEFQQmdOVkhSTUJBZjhFQlRBREFRSC9NQjBHQTFVZERnUVcKQkJUT3VzZFZTMzB5WTI3NFE5enFQY1NicmUwZTNEQU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FRRUF2dUFOR3RZdwo4ck5rbkFzWVVGNGsySWp0TDhqM3ZDMzkvZXNHMi9vWlloUFlRbmVyWlBxMlpVZ3JwSTFoQ3E1aWd0cTFZQ2p3CkF6QWJScy9yb1E0VjdIMWYxUkZYQzd3ZjlJUGs1TWdpdTQxTWtsd3FBZ3liMkk3RU41TWlyQ1dMaVY1Ukc4K1oKWFgrWHk0VFFicjRRYmduODFObGViV2pRaVhVcjBYK0hTNUJHclAxd1VZWFZGU1BLQXBkTVZUd3V3bUVOSXRTVwpaRWUyTnBlY05zSkJwVlZ4b2FNb0xzU1kwaFRnclV5ckNYNXZzaloxZVZ4VHRYYVJHRmozcUwzL3h6WW1US3BzCnRmQVp3R3FmWDhpdEsvcUFPRythVDdzS0ZQeUp5YWNkQm1FNjFZRC9lUTVQNWc4WGFWVkVyWE5kM09mNTI2NjAKOTc2ZG1MUG9VcDZGT1E9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==''', clusterName: 'minikube', contextName: '', credentialsId: 'k8sconfig', namespace: '', restrictKubeConfigAccess: false, serverUrl: 'https://192.168.49.2:8443') {
                    sh ' kubectl apply -f manifest.yaml'
                }

            }
        }
    }
}