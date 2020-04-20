while True:
	try:
		check1or2 = int(input("If you are single please input '1', if not please input '2': "))

		if check1or2 == 1:
			while True:
				try:
					# Only one people
					income = int(input("Please enter your taxable income: "))

					allowance = 132000

					if income*0.05 > 18000:
						mpf = 18000
					else:
					   mpf = income*0.05
					# mpf is 5% of income but should not be greater than 18000

					print("Your mpf is $",mpf)

					#This is separate assessment
					netchargeableincome = income - mpf - allowance

					if netchargeableincome < 0:
						tax = 0


					elif netchargeableincome <= 50000:
						tax = netchargeableincome * 0.02

					elif netchargeableincome <= 100000:
						tax = (netchargeableincome - 50000) * 0.06 + 1000

					elif netchargeableincome <= 150000:
						tax = (netchargeableincome - 100000) * 0.1 + 4000

					elif netchargeableincome <= 200000:
						tax = (netchargeableincome - 150000) * 0.14 + 9000

					else:
						tax = (netchargeableincome - 200000) * 0.17 + 16000
						if tax > (income - 18000) * 0.15:
							tax = (income - 18000) * 0.15
							print("Standard rate is used for you")

					print("You need to pay $", tax, "dollars")
					break
				except ValueError:
					print("Sorry, Please input a right number again")

					continue



		elif check1or2 == 2:
			while True:
				try:

					income = int(input("Please enter your taxable income: "))
					income2 = int(input("Please enter your spouse taxable income: "))

					allowance = 132000

					if income*0.05 > 18000:
						mpf = 18000
					else:
					   mpf = income*0.05
					# mpf is 5% of income but should not be greater than 18000

					if income2*0.05 > 18000:
						mpf2 = 18000
					else:
					   mpf2 = income2*0.05

					print("Your mpf is $",mpf)
					print("Your spouse's mpf is $", mpf2)

					#This is separate assessment
					netchargeableincome = income - mpf - allowance
					netchargeableincome2 = income2 - mpf2 - allowance


					if netchargeableincome < 0:
						tax = 0

					elif netchargeableincome <= 50000:
						tax = netchargeableincome * 0.02

					elif netchargeableincome <= 100000:
						tax = (netchargeableincome - 50000) * 0.06 + 1000

					elif netchargeableincome <= 150000:
						tax = (netchargeableincome - 100000) * 0.1 + 4000

					elif netchargeableincome <= 200000:
						tax = (netchargeableincome - 150000) * 0.14 + 9000

					else:
						tax = (netchargeableincome - 200000) * 0.17 + 16000
						if tax > (income - 18000) * 0.15:
							tax = (income - 18000) * 0.15
							print("Standard rate is used for you")

					if netchargeableincome2 < 0:
						tax2 = 0

					elif netchargeableincome2 <= 50000:
						tax2 = netchargeableincome2 * 0.02

					elif netchargeableincome2 <= 100000:
						tax2 = (netchargeableincome2 - 50000) * 0.06 + 1000

					elif netchargeableincome2 <= 150000:
						tax2 = (netchargeableincome2 - 100000) * 0.1 + 4000

					elif netchargeableincome2 <= 200000:
						tax2 = (netchargeableincome2 - 150000) * 0.14 + 9000

					else:
						tax2 = (netchargeableincome2 - 200000) * 0.17 + 16000
						if tax2 > (income2 - 18000) * 0.15:
								tax2 = (income2 - 18000) * 0.15
								print("Standard rate is used for your spouse")


					totaltax = tax + tax2
					# This is joint assessment
					totalincome = income + income2
					netchargeableincome3 = totalincome - mpf - mpf2 - allowance*2



					if netchargeableincome3 <= 0 :
						print ("You don't need to pay any tax for joint assessment")
					else :
						if netchargeableincome3 <= 50000:
							tax3 = netchargeableincome3 * 0.02

						elif netchargeableincome3 <= 100000:
							tax3 = (netchargeableincome3 - 50000)* 0.06 + 1000

						elif netchargeableincome3 <= 150000:
							tax3 = (netchargeableincome3 - 100000) * 0.1 + 4000

						elif netchargeableincome3 <= 200000:
							tax3 = (netchargeableincome3 - 150000) * 0.14 + 9000

						else:
							tax3 = (netchargeableincome3 - 200000) * 0.17 + 16000

							if tax3 > (totalincome - 36000)*0.15 :
								tax3 = (totalincome - 36000)*0.15
								print("Standard rate is used for joint assessment")


					if netchargeableincome + netchargeableincome2 < 0:
						print("You don't have to pay tax for separate assessment")
					#under separate assessment
					else:
						print("Under separate taxation, You should pay $",tax, "dollars.")
						print("Under separate taxation, Your Spouse should pay $", tax2, "dollars.")
						print("In total, you have to pay $", totaltax, "dollars under separate taxation.")
						print("Under joint assessment, You need to pay $", tax3,"dollars in total !")

						if totaltax < tax3 :
							print("You are recommended to use separate assessment for $",totaltax)
						else :
							print("You are recommended to use joint assessment for $",tax3)
					break

				except ValueError:
					print("Sorry, Please enter a number")

					continue
	except ValueError:
					print("Sorry, Please enter a number")

					continue
