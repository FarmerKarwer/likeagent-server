console.log('Hello!!!!!!!')
const url = window.location.href

const quizBox = document.getElementById('quiz-box')
let data

$.ajax({
	type: 'GET',
	url: `${url}data/`,
	success: function(response){
		// console.log(response)
		data = response.data
		data.forEach(el => {
			for (const [question, answers] of Object.entries(el)){
				quizBox.innerHTML += `
				<p>
				<div class="quiz-question-header">
					<h3 class="quiz-question-title">${question}</h3>
				</div>
				</p>
				`
				answers.forEach(answer=>{
					quizBox.innerHTML += `
					<div class="col-4 col-12-small">
					<input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
					<label for="${question}-${answer}">${answer}</label>
					</div>
					`
				})
			}
		});
	},
	error: function(error){
		console.log(error)
	}
})