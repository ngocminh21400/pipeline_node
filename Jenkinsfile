
pipeline{
    agent {label 'centos-vm'}

    stages{
        stage('Git update'){
            steps{
                sh 'cat /etc/os-release'
                git 'https://github.com/ngocminh21400/pipeline_node.git'

                echo 'Clone Done..'
            }
        }

        stage('Docker build'){
            steps{
                echo 'Building..'

                withDockerRegistry(credentialsId: 'docker-id') {
                    sh 'docker build -t my-node .'
                    sh 'docker tag my-node mingming21400/my-node:v1.1'
                    sh 'docker push mingming21400/my-node:v1.1'
                    sh 'docker run -d -p 4000:4000 --name my-node mingming21400/my-node'
                    sh 'docker exec -u root my-node /bin/bash'
                }

                script{
                    try{
                        sh 'docker ps'
                        sh 'curl localhost:4000'
                    }catch(Exception e){
                        echo e.toString()
                    }
                }
            }
        }
        stage('Test'){
            steps{
               sh """
                   

               """
            }
        }

    }  
    post {
        always {
            sh 'docker stop my-node'
            sh 'docker container prune --force'
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