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
                //sh 'docker run gesellix/trufflehog --json https://github.com/georgesb1/SecDevOps.git > trufflehog'
                //sh 'cat trufflehog'
            }
        }
        
        stage("Source Composition Analysis"){
            steps{
                sh ' rm Owasp* || true'
                //sh ' wget https://raw.githubusercontent.com/georgesb1/SecDevOps/main/Owasp-dependency-check.sh '
                //sh 'chmod +x Owasp-dependency-check.sh'
                //sh 'bash Owasp-dependency-check.sh'
                //sh 'cat /home/kali/OWASP-Dependency-Check/reports/dependency-check-report.xml'
            }
        }

       // stage('SAST with SonarQube ') {
         //   steps {
           //     script {
             //       def scannerHome = tool 'sonar-scanner'
               //     withSonarQubeEnv('Sonarqube') {
                 //       sh "${scannerHome}/bin/sonar-scanner"
                   // }
               // }
           // }
       // }

        stage("Build") {
            steps {
                script {
                    def harborPassword = credentials('harbor')

                    sh "echo ${BUILD_NUMBER}"
                    sh "docker build -t chatbot:${BUILD_NUMBER} ."

                    // Use the credentials for Docker login
                    withCredentials([string(credentialsId: 'harbor', variable: 'HARBOR_PASSWORD')]) {
                        sh "docker login https://core.harbor.domain:32331/ -u admin -p ${HARBOR_PASSWORD}"
                    }

                    sh "docker tag chatbot:${BUILD_NUMBER} core.harbor.domain:32331/registry/chatbot:${BUILD_NUMBER}"
                    sh "docker push core.harbor.domain:32331/registry/chatbot:${BUILD_NUMBER}"
                }
            }
        }


        stage("DAST with OWASP ZAP"){
            steps{
                sh ' rm report.xml || true'
                sh ' echo yes '
            }
        }
    }
}