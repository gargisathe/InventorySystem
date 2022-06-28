Bot.send('Hey, Welcome to St Judes!!');
Bot.send('Press Yes to continue');
var state = 0;
var name, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11;
var response = [];
var count = 0;

async function respond(inputText) {
	if (state == '0') {
		if (inputText == 'yes') {
			Bot.send('Please enter your name!');
			state = 1
		}

	}

	else if (state == '1') {
		name = inputText;
		Bot.send('Please enter UID mentioned on Aadhar Card')
		state = 2
	}

	else if (state == '2') {
		ans1 = inputText;
		Bot.send('Do you wish to Rebook Ration?')
		state = 3
	}
	else if (state == '3') {
		ans2 = inputText;
		Bot.send('Do you wish raise funds for medical purposes?')
		state = 4
	}
	else if (state == '4') {
		ans3 = inputText;
		Bot.send('Do you wish to book occupancy room in our assocated cities?');
		state = 5
	}

		response[0] = await CampK12.classify("mental health model", ans1);
		response[1] = await CampK12.classify("mental health model", ans2);
		response[2] = await CampK12.classify("mental health model", ans3);
		response[3] = await CampK12.classify("mental health model", ans4);
		response[4] = await CampK12.classify("mental health model", ans5);
		response[5] = await CampK12.classify("mental health model", ans6);
		
	}

