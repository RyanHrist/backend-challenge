echo "******************************************"
echo "--------Installing Dependcencies...-------"
echo "******************************************"
pip3 install -r requirement.txt
pip3 install requests
pip3 install datetime

echo "******************************************"
echo "-----Initializing/Clearing Database...----"
echo "******************************************"
python3 initiate_db.py

echo "******************************************"
echo "-------------Run Tests...-----------------"
echo "******************************************"
python3 test_conversation.py