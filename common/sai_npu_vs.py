import time
from sai_npu import SaiNpu


class SaiNpuVs(SaiNpu):

    def __init__(self, exec_params):
        super().__init__(exec_params)

    def reset(self):
        self.cleanup()
        time.sleep(5)
        attr = [
            "SAI_SWITCH_ATTR_SRC_MAC_ADDRESS",      "52:54:00:EE:BB:70",
            "SAI_SWITCH_ATTR_FDB_AGING_TIME",       "600",
            "SAI_SWITCH_ATTR_TPID_INNER_VLAN",      "33024",    # 0x8100
            "SAI_SWITCH_ATTR_TPID_OUTER_VLAN",      "34984",    # 0x88A8
            "SAI_SWITCH_ATTR_VXLAN_DEFAULT_PORT",   "4789"
        ]
        self.init(attr)

