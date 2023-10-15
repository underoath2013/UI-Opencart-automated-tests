pipeline {
    agent any

    environment {
        ALLURE_PATH = '/home/linuxbrew/.linuxbrew/bin/allure'
    }

    parameters {
        string(name: 'EXECUTOR_ADDRESS', defaultValue: 'http://selenoid:4444/wd/hub', description: 'Address of the Selenoid executor')
        string(name: 'APP_URL', defaultValue: 'http://192.168.0.109:8081', description: 'URL of the OpenCart application')
        string(name: 'THREADS', defaultValue: '1', description: 'Number of threads')
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Browser type')
        string(name: 'BROWSER_VERSION', defaultValue: '115', description: 'Browser version')
        string(name: 'ALLURE_RESULTS', defaultValue: 'allure-results', description: 'Path to Allure results directory')
        string(name: 'ALLURE_REPORT', defaultValue: 'allure-report', description: 'Path to Allure report directory')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM',
                branches: [[name: '*/main']],
                extensions: [],
                submoduleCfg: [],
                userRemoteConfigs: [[url: 'https://github.com/underoath2013/UI-Opencart-automated-tests.git']]])
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh """
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pytest --browser \${BROWSER} --bv \${BROWSER_VERSION} --url \${APP_URL} -n \${THREADS} --remote --remote_url \${EXECUTOR_ADDRESS} --alluredir \${ALLURE_RESULTS}
                        """
                    } finally {
                        sh "\${ALLURE_PATH} generate \${ALLURE_RESULTS} -c -o \${ALLURE_REPORT}"
                    }
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: "${ALLURE_RESULTS}"]]
                ])
            }
        }
    }
}
