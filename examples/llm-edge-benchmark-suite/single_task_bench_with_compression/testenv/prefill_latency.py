from sedna.common.class_factory import ClassType, ClassFactory

__all__ = ["prefill_latency"]

@ClassFactory.register(ClassType.GENERAL, alias="prefill_latency")
def prefill_latency(y_true, y_pred):
    # avg_prefill_latency = y_pred.get('avg_prefill_latency', [])
    # return avg_prefill_latency
    #TODO 前面所有歌predict_dict 的结果，可以通过下面拿出来，我想把计算平均的过程放在这里，帮我实现
    results_list = y_pred.get('results', [])
    num_requests = len(results_list)
    total_prefill_latency = 0.0
    for result in results_list:
        total_prefill_latency += result['prefill_latency']
    avg_prefill_latency = total_prefill_latency / num_requests
    return avg_prefill_latency