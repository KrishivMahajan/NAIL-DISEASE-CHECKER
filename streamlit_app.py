import streamlit  as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="CutiCure", page_icon=":medical_symbol:", layout="wide")

tb1, tb2, tb3 =st.tabs(["HOME", "DISEASE DETECTOR", "ABOUT ME"])

with tb1:
	st.title(":medical_symbol: CutiCure")
	st.write("  To Use the model, go to the 'DISEASE DETECTOR' tab")
	st.write("---")
	st.header("NAILS AND THEIR IMPORTANCE")
	cl1=st.columns([0.7,0.3])
	cl1[1].image("Nails.JPG")
	cl1[0].write(
		"""
		Nails are protective structures composed of a protein called keratin that grow at the tips of the fingers and toes in humans and other mammals. They serve several important functions:

	- Protection: Nails provide protection to the sensitive tips of the fingers and toes. They act as a shield to prevent injuries or damage to the underlying tissues.
	- Sensory Function: Nails also have a sensory function, particularly in the fingertips where they play a role in tactile sensation. The fingertips are highly sensitive, and nails help enhance touch perception.
	- Grip and Manipulation: Nails enhance our ability to grip and manipulate objects. They provide a firm, non-slip surface that helps us hold onto items, such as when picking up small objects or opening containers.
	- Scratching: Nails can be used for scratching, which can be a useful function for relieving itching or removing debris from the skin.
	- Health Indicator: The appearance of nails can sometimes serve as an indicator of overall health. Changes in nail color, texture, or growth patterns can be associated with various health conditions or nutritional deficiencies.
	- Cosmetic and Aesthetic Value: For many people, well-maintained nails are an important aspect of personal grooming and aesthetics. Manicures and pedicures are popular beauty treatments to enhance the appearance of nails.
		"""
	)
	
	st.write("---")
	cl2=st.columns([0.3,0.7])
	cl2[0].image("Disease.JPG",width=340)
	cl2[1].header("WHY IS IT IMPORTANT TO DETECT THEM")
	cl2[1].write(
		"""
		- Early Intervention: Detecting nail diseases early can lead to more effective treatment and better outcomes. In many cases, early intervention can prevent the condition from worsening or spreading to other nails.
	- Underlying Health Issues: Changes in nail appearance can sometimes be a sign of underlying health conditions, such as fungal infections, psoriasis, or nutritional deficiencies. Identifying these signs can prompt further medical evaluation, which may lead to the diagnosis and treatment of other health problems.
	- Prevention: Identifying and treating nail diseases can help prevent complications. For example, fungal nail infections can lead to secondary bacterial infections or the spread of the infection to other parts of the body if left untreated.
	- Quality of Life: Nail diseases can be uncomfortable, painful, or unsightly. Addressing these conditions can improve a person's overall quality of life, reduce discomfort, and enhance self-esteem.
	- Infection Control: Some nail diseases, such as fungal infections, can be contagious. Prompt detection and treatment can help prevent the spread of these infections to others.
	- Avoiding Complications: Certain nail conditions, if left untreated, can lead to complications, such as cellulitis (a skin infection), abscesses, or chronic pain. Addressing these issues promptly can prevent these complications.
	- Monitoring Chronic Conditions: For individuals with chronic skin conditions like psoriasis or eczema, monitoring the nails is essential as they can be affected. Catching nail-related symptoms early allows for better management of the underlying skin condition.
	- Personal Grooming and Well-Being: Many people take pride in their personal grooming, and healthy nails are a part of that. Maintaining the health and appearance of nails can contribute to a person's overall well-being and self-confidence.
	"""
	)
	
	
with tb2:
	st.markdown("""HOW TO USE THE APP
- Click on Browse Files
- Click a clear picture of your nail or select from your gallery if already clicked
- Upload the image 
- The model will predict the disease
 """)
	dic={

"Acral Lentiginous Melanoma": "Acral lentiginous melanoma (ALM) is a rare subtype of melanoma arising on the palms, soles, or under the nails. It is also known as acral melanoma",
"Beaus Line": "Beau's lines are transverse depressions or ridges that run horizontally across the nails. They can be caused by a variety of factors, including illness, trauma, or nutritional deficiencies. The appearance of Beau's lines can offer insight into the timing of an underlying health issue.",
"Blue Finger": "It is a benign and rare condition with an idiopathic aetiology. Blue finger can mean your organs, muscles and tissues aren’t getting the amount of blood they need to function properly. Many different conditions can cause cyanosis.",
"Clubbing": "Nail clubbing is characterized by an enlargement of the fingertips and a downward curving of the nails. It can be associated with various lung and heart conditions. If clubbing is observed, it is important to consult a healthcare professional to identify and address the underlying issue.",
"Koilonychia": "Koilonychia is a condition where the nails become concave or spoon-shaped. It can be a sign of iron deficiency anaemia or hemochromatosis, among other conditions. Treating the underlying cause is essential.",
"Lindsay-s Nail": "Half and half nails  show the proximal portion of the nail white and the distal half red, pink, or brown, with a sharp line of demarcation between the two halves",
"Muehrckes Lines": "Muehrcke's lines appear as double white lines that run across the fingernails horizontally. The lines have been linked to low levels of a protein called albumin.",
"Onychogryphosis": "Onychogryphosis, also known as ram’s horn nail, is a nail disorder resulting from slow nail plate growth. Onychogryphosis is a nail disease that causes one side of the nail to grow faster than the other. ",
"Pitting": "Nail pitting may show up as shallow or deep holes in your nails. The pitting can happen on your fingernails or your toenails. It's common in people who have skin disorders such as psoriasis and eczema.",
"Terry-s Nail": "Terry’s nails is a type of nail discolouration. Terry’s nails is a symptom of a chronic condition, such as liver failure or diabetes. Sometimes, it is a sign of aging."
}
	st.header("TEST YOURSELF")
	img=st.file_uploader("UPLOAD THE IMAGE OF YOUR NAIL")
	if img is not None:
		col=st.columns(3)
		col[1].image(img)
		#img1=img.getvalue()
		img2=Image.open(img)
		import inference
		model = inference.get_model("nail-diseases-wnxuv/1")
		pred=model.infer(image=img2)
		name = (pred[0].predicted_classes[0])
		con = pred[0].predictions.get(name)
		col = st.columns(2)
		with col[0]:
			st.subheader('Prediction')
			st.write(name)
		with col[1]:
			st.subheader('Confidence')
			st.write(con.confidence)
		st.write(dic.get(name))

with tb3:
	st.header("ABOUT THE CREATOR")
	col = st.columns(3)
	col[1].image("My.jpg")
	st.write(
		"""
		Greetings! I'm Krishiv Mahajan, a passionate grade 11 student at Sat Paul Mittal School with a profound love for computer science and an unwavering desire to make a positive impact in people's lives. As I embark on this journey, my mission is crystal clear - to combine the power of technology with a heartfelt commitment to your well-being.
	In a world where health takes precedence, I've set out to create a dedicated space where your nail health is at the forefront. Nails are often the silent messengers of underlying health issues, and my aim is to empower you with the tools to detect diseases early and take control of your well-being.
	My dedication to the world of computer science fuels my pursuit of innovation and excellence. I believe that technology can be a force for good, and together, we can harness its potential to revolutionize how we care for our nails and, in turn, our overall health.
	With the Nail Disease Detection website, I aspire to provide a valuable resource for everyone. Whether you're seeking answers to your nail-related concerns or simply want to stay informed about your health, you'll find a supportive community here.
		"""
	)

