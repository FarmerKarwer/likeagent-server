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

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
	const elements = [...document.getElementsByClassName('ans')]
	const data = {}
	data['csrfmiddlewaretoken'] = csrf[0].value
	elements.forEach(el=>{
		if (el.checked){
			data[el.name] = el.value
		} else {
			if (!data[el.name]) {
				data[el.name] = null
			}
		}
	})
	$.ajax({
		type: 'POST',
		url: `${url}save/`,
		data: data,
		success: function(response){
			console.log(response)
		},
		error: function(error){
			console.log(error)
		}
	})
}

quizForm.addEventListener('submit', e=>{
	e.preventDefault()

	sendData()
})