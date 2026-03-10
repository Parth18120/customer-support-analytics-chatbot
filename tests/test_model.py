from chatbot.model import ChatbotModel


def test_known_intent_prediction():
    model = ChatbotModel(confidence_threshold=0.20)
    result = model.predict("I forgot my password")
    assert result.intent == "account_help"
    assert result.fallback is False


def test_low_confidence_triggers_fallback():
    model = ChatbotModel(confidence_threshold=0.95)
    result = model.predict("Tell me about the moon landing")
    assert result.fallback is True
    assert result.intent == "fallback"
