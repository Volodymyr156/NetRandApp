import random
import requests

# domain_sellers = ["https://forsale.godaddy.com","https://www.cscdbs.com", "https://sedo.com", "https://www.afternic.com", "https://forsale.dynadot.com", "https://brandpa.com", "https://www.hugedomains.com", "https://www.domainmarket.com", "https://www.brandbucket.com"]
# errors = ["Origin is unreachable", "This Page Is Under Construction ? Coming Soon! Why am I seeing this 'Under Construction' page? ", "403 Forbidden The region has been denied."]
code_200 = []
code_bad = []
list_numbers = [str(x) for x in range(10)]
list_chars = [chr(x) for x in range(97,123)]
# str_symbols = "~._-"
# with open("dictionary.json", "r") as file:
#     english_dictionary = json.load(file)



def link_gen(link_input):
    protocol = link_input[0]
    k_chars = int(link_input[1])
    k_numbers = int(link_input[2])
    domain = link_input[3]
    i = int(link_input[4])

    print(protocol,k_chars,k_numbers,domain)

    while i > 0:
        loop_chars = random.sample(list_chars, k= k_chars)
        loop_numbers = random.sample(list_numbers, k=k_numbers)
        loop_chars_numbers = loop_chars + loop_numbers
        random.shuffle(loop_chars_numbers)

        str_chars_numbers = "".join(loop_chars_numbers)

        generated_url = protocol + str_chars_numbers + domain

        if generated_url not in code_200 and generated_url not in code_bad:
            try:
                request = requests.get(generated_url)
                print(f"Working URL: ************{generated_url}************")
                code_200.append(generated_url)
                i -= 1


            except:
                print(f"Bad Url: {generated_url}")
                code_bad.append(generated_url)

    print(f"Loop completed")



