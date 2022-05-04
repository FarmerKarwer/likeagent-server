console.log('Hello!!!!!!!')
const url = window.location.href

const quizBox = document.getElementById('quiz-box')
const additionalBox = document.getElementById('additional-box')
const resultBox = document.getElementById('result-box')
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
					<input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}" required="required">
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

// Getting additional data

$.ajax({
	type: 'GET',
	url: `${url}additional_data/`,
	success: function(response){
		data = response.data
		data.forEach(el => {
			for (const [question, answers] of Object.entries(el)){

				additionalBox.innerHTML += `
				<div class="col-12">
					<select class="addque" name="${question}" id="${question}">
						<option value="${question}" disabled selected>- ${question} -</option>
				`
				q = document.getElementById(question)
				answers.forEach(answer=>{
					q.innerHTML += `
					<option name="${question}" class="addans" value="${answer}">${answer}</option>
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
const main_description = document.getElementById('main-description')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


// Sending additional data

const sendAdditionalData = () => {
	const elements = [...document.getElementsByClassName('addans')]
	const head_elements = [...document.getElementsByClassName('addque')]
	const data = {}
	data['csrfmiddlewaretoken'] = csrf[0].value
	head_elements.forEach(hel=>{

		elements.forEach(el=>{
			console.log(el)
			console.log(el.value)
			if (hel.options[hel.selectedIndex].value == el.value){
				data[hel.name] = el.value
			} else {
				if (!data[hel.name]) {
					data[hel.name] = null
				}
			}
		})

	})

	$.ajax({
		type: 'POST',
		url: `${url}save_additional_data/`,
		data: data,
		success: function(response){
			console.log(response)
		},
		error: function(error){
			console.log(error)
		}
	})

}


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
			const results = Object.entries(response);
			console.log(results)
			quizForm.classList.add('not-visible')
			main_description.classList.add('not-visible')
			resultBox.innerHTML += `<h2>Результат:</h2>`
			// Object.entries(response).forEach(res=>{
			 	const resDiv = document.createElement("div")
				for (const [question, resp] of results){

					const description = resp['description']
					const res_name = resp['name']
					const res_text = resp['text']

				resultBox.innerHTML += `
				<p>${description}</p>
				<h4>${res_name}</h4>
				<p>${res_text}</p>
				
				`

				}

		resultBox.innerHTML += `<hr>`
		},
		error: function(error){
			console.log(error)
		}
	})
}

quizForm.addEventListener('submit', e=>{
	e.preventDefault()

	sendData()
	sendAdditionalData()
})