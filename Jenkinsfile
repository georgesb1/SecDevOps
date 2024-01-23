pipeline {
    agent any 

    stages {
        stage("Checkout") {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git']])
            }
        }

        stage("CheckSecret") {
            steps {
                sh 'rm trufflehog || true'
                // sh 'docker run gesellix/trufflehog --json https://github.com/georgesb1/SecDevOps.git > trufflehog'
                // sh 'cat trufflehog'
            }
        }
        
        stage("Source Composition Analysis") {
            steps {
                sh 'rm Owasp* || true'
                // sh 'wget https://raw.githubusercontent.com/georgesb1/SecDevOps/main/Owasp-dependency-check.sh'
                // sh 'chmod +x Owasp-dependency-check.sh'
                // sh 'bash Owasp-dependency-check.sh'
                // sh 'cat /home/kali/OWASP-Dependency-Check/reports/dependency-check-report.xml'
            }
        }

        stage('SAST with SonarQube ') {
            steps {
                sh " true "
              //   script {
                //     def scannerHome = tool 'sonarqube'
                  //   withSonarQubeEnv('sonarqube') {
                    //     sh "${scannerHome}/bin/sonar-scanner"
                    // }
                // }
            }
        }

        stage("Build") {
            steps {
                 script {
                     def harborPassword = credentials('harbor')
                     sh "echo ${BUILD_NUMBER}"
                     sh "docker build -t chatbot:${BUILD_NUMBER} ."
                     withCredentials([string(credentialsId: 'harbor', variable: 'HARBOR_PASSWORD')]) {
                        sh "docker login https://core.harbor.domain:31089/ -u admin -p ${HARBOR_PASSWORD}"
                        }
                     sh "docker tag chatbot:${BUILD_NUMBER} core.harbor.domain:31089/myregistry/chatbot:${BUILD_NUMBER}"
                     sh "docker push core.harbor.domain:31089/myregistry/chatbot:${BUILD_NUMBER}"
                 }
            }
        }

        stage("DAST with OWASP ZAP") {
            steps {
                sh 'rm report.xml || true'
                sh 'echo yes'
            }
        }

        stage("Deploy on kubernetes") {
            steps {
                sh ' true '
                withKubeConfig(caCertificate: 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCakNDQWU2Z0F3SUJBZ0lCQVRBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwdGFXNXAKYTNWaVpVTkJNQjRYRFRJek1USXlOVEU0TkRJeU5Wb1hEVE16TVRJeU16RTROREl5TlZvd0ZURVRNQkVHQTFVRQpBeE1LYldsdWFXdDFZbVZEUVRDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTVVKCjdPb2hrbW5oYUVxQjh5eHRuanZuOWtVcnBPWGt2QlZyNUsyTkpOa0ZkN1R4NlhVWlJqOVdsRStuaU5ZVktLR3cKbnFnanFtN3pNMWpNdkFLMjJhUEFVN0pnN0E5bWVTUGNaQ2lCMkk2OVhwZHRDckF4UWlycGthYVpCNDBxQU5TYgpyVWNWMVRNTVYrczZKeXBlYmZsTVRWR09yMlh5SlJzTjgrSTR2Ky9TQnE2L0xsSzZKMG1WZ2lqTy9IU1hJWG5LCk83ekRzS2k5Q2pNU1RncFlrMEcxSFFqNWROSUxGdGxsZE1mdVl1TjBwb0xOTmlOM3Y1YXlyZkJkTlVWMHNBR2kKekdRQVlPM3Z3RG9xNVZOVmNQOHlHVGhOYjE5K1JhUFltSlVPVE5YdXdqUTF6bzdoMkIyYXdBelVTMnk4NzRVMAp2Z3pFOHdTa1JJS255YlNpRkZFQ0F3RUFBYU5oTUY4d0RnWURWUjBQQVFIL0JBUURBZ0trTUIwR0ExVWRKUVFXCk1CUUdDQ3NHQVFVRkJ3TUNCZ2dyQmdFRkJRY0RBVEFQQmdOVkhSTUJBZjhFQlRBREFRSC9NQjBHQTFVZERnUVcKQkJSTlRkUWtIZEJtMXc3WHBsR0t3K2EzTFZ4RGdqQU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FRRUFMdmlSbkl3TgpYMjFVTDMwTFdRT2xObHY4RVpyenhCeXoxa05yYTB0QUxqOEgxSUZjb1p2Q0NxWUpiY3lPWUtNRnorNmNTMUthCjhtUEwycFFyREZtMzlpLzBnNWNEajJSRUtabEM1SFVqREprbmt4b2RrRGd0QUR3Z1ZZZDZpTFhXTHVTZnFnZk4KbjFtVlVJdUtCd2FreEdJQUx3R2gxY0tjSFA1eEdlc0pVNnN0RW9tdGxPWGE0UUswZzVnTnFKT3dVYmgrVmlJZwpYNVJZdEJyWCtGSW11RDhEUUg1UVdwRFhZemNZSU1xZWRTY2xWWURldUtKVmZudnkvb1ZDeVN4eEpGdzBGdjdICjQ2a1A4cisyNGl5ZG9zUkw2UUtObElYcjc3RERoNzB2dGtNUzF5RGl3VDk2eEhOSGhWdmR1TUZ4bTZwQWZBZEoKRldkbFRsbys5UTErekE9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==', clusterName: 'minikube', contextName: 'minikube', credentialsId: 'k8sconfig', namespace: '', restrictKubeConfigAccess: false, serverUrl: 'https://192.168.49.2:8443') {
                    sh 'kubectl apply -f manifest.yaml'
                }
            }
        }
    }
}
