pipeline{
    agent {label 'centos-vm'}

    stages{
        stage('Git update'){
            steps{
                sh 'cat /etc/os-release'
                git 'https://github.com/ngocminh21400/pipeline_node.git'

                // def version = version()
                // if(version){
                //     "Building version ${version}"
                // }

                echo 'Clone Done..'
            }
        }

        stage('Docker build'){
            steps{
                echo 'Building..'

                withDockerRegistry(credentialsId: 'docker-id') {
                    sh 'docker build -t my-node .'
                    sh 'docker tag my-node mingming21400/my-node:v1.0'
                    sh 'docker push mingming21400/my-node:v1.0'
                    sh 'docker run -d -p 4000:4000 --name my-node mingming21400/my-node'
                    try{
                        sh 'curl localhost:4000'
                    }catch{}
                    
                    // sh 'docker stop angular'
                    // sh 'docker rm angular'
                }
            }
        }
        stage('Test'){
            steps{
                script{
                    int i = 0
                    timeout(time: 5, unit: 'SECONDS') {
                        retry(5) {
                            echo 'Testing... ${i}'
                            i++
                        }
                    }
                }

            }
        }

    }  
    post {
        always {
            echo 'One way or another, I have finished'
            deleteDir() /* clean up our workspace */
        }
        success {
            echo 'I succeeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    } 
}