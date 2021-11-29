
pipeline{
    parameters {
        choice(name : 'AGENT',choices: ['centos-vm' ,'master'], description: 'Choose node to run job')

        choice(name: 'REPEAT_TIMES', choices: [1,2,3,4], description: 'Choose times to repeat get API test')
        
        booleanParam(name: 'CHECKOUT_CODE', defaultValue: true)
    }

    agent {label params.AGENT == "any" ? "" : params.AGENT}

    stages{
        stage('Git update'){
            when { 
                params.AGENT == true
            }
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
   
                }
            }
        }

        stage('Test'){
            when{
                beforeAgent true
            }
            steps{
               script{
                    try{
                        sh 'curl localhost'
                    }catch(Exception e){
                        echo "ERROR TEST"
                        echo e.toString()
                    }
                     try{
                        sh 'curl localhost:4000'
                    }catch(Exception e){
                        echo "ERROR TEST"
                        echo e.toString()
                    }
                }

                sh "python3 ./test/test1.py"
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