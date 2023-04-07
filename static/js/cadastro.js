const form = document.getElementById("form");
const nameClient = document.getElementById("nameClient");
const birthdate = document.getElementById("birthdate");
const cpf = document.getElementById("cpf");
const email = document.getElementById("email");
const celphone = document.getElementById("celphone");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  checkInputs();
});

function checkInputs() {
  const nameClientValue = nameClient.value;
  const birthdateValue = birthdate.value;
  const cpfValue = cpf.value;
  const emailValue = email.value;
  const celphoneValue = celphone.value;

  if (nameClientValue === "") {
    setErrorFor(nameClient, "O seu nome completo é obrigatório.");
  } else {
    setSuccessFor(nameClient);
  }

  if (birthdateValue === "") {
    setErrorFor(birthdate, "A sua data de nascimento é obrigatória.");
  } else {
    setSuccessFor(birthdate);
  }

  if (cpfValue === "") {
    setErrorFor(cpf, "O seu CPF é obrigatório.");
  } else if (cpfValue.length != 11) {
    setErrorFor(cpf, "Por favor, insira um CPF válido.");
  } else {
    setSuccessFor(cpf);
  }

  if (emailValue === "") {
    setErrorFor(email, "O seu e-mail é obrigatório.");
  } else if (!checkEmail(emailValue)) {
    setErrorFor(email, "Por favor, insira um e-mail válido.");
  } else {
    setSuccessFor(email);
  }

  if (celphoneValue === "") {
    setErrorFor(celphone, "O seu número de celular é obrigatório.");
  } else {
    setSuccessFor(celphone);
  }

  const formControls = form.querySelectorAll(".form-control");

  const formIsValid = [...formControls].every((formControl) => {
    return formControl.className === "form-control success";
  });

  if (formIsValid) {
    console.log("O formulário está 100% válido!");
  }
}

function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const small = formControl.querySelector("small");

  // Adiciona a mensagem de erro
  small.innerText = message;

  // Adiciona a classe de erro
  formControl.className = "form-control error";
}

function setSuccessFor(input) {
  const formControl = input.parentElement;

  // Adicionar a classe de sucesso
  formControl.className = "form-control success";
}

function checkEmail(email) {
  return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
    email
  );
}