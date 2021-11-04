from characteristics.models import *


def get_queryset_for_all_characteristic():


    return {
        "diagonal_screen" : ScreenDiagonal.objects.all(),
        "screen_type" : ScreenType.objects.all(),
        "screen_frequency" : ScreenFrequency.objects.all(),
        "processor_name" : ProcessorType.objects.all(),
        "operation_system" : OperationSystem.objects.all(),
        "memory_capacity" : MemoryCapacity.objects.all(),
        "memory_slots" : MemorySlot.objects.all(),
        "memory_type" : MemoryType.objects.all(), 
        "data_storage" : DataStorageDevices.objects.all(),
        "video_card" : VideoCard.objects.all(),
        "video_card_memory" : VideoCardMemory.objects.all()
    }