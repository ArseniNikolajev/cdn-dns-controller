pipelane {
	environment {
			repository = "https://github.com/ArseniNikolajev/cdn-dns-controller"
			repositoryCredentails = "prikop5cm"
			
	}
	agent any 
	options {
		timeout(time: 1, unit: 'HOURS')
	}
	stages { 
	stage('git clone') {
		step {
			git credentailsID: ${repositoryCredentails}
				url:${repository}
			}
		}
		
	stage('tests') {
		steps {
			sh ''python3 -m pytest tests/'
		}
	}
	stage ('create docker image'){
		step {
			sh 'docker build -t cdn-dns-controller -fg docker/Dockerfile .'
		}
	}
	
	stage ('run docker'){
		step {
			sh 'docker run -it -d -[ 5000:5000 --rm --name cdn-dns-controller cdn-dns-controller'
		}
	}
	stage('sanity test'){
		step {
			sh 'curl localhost:5000/'
		}
	}
	stage ('cleanup') {
		steps {
			sh 'docker rm -f cdn-dns-controller'
			}
		}
	}
}