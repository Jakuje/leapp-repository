from leapp.actors import Actor
from leapp.libraries.actor.library import remove_boot_entry
from leapp.models import BootContent
from leapp.tags import InitRamStartPhaseTag, IPUWorkflowTag


class RemoveUpgradeBootEntry(Actor):
    """
    Remove boot entry for Leapp provided initramfs.

    After upgrade process used initramfs after reboot, this entry is not necessary anymore.
    """

    name = 'remove_upgrade_boot_entry'
    consumes = (BootContent,)
    produces = ()
    tags = (IPUWorkflowTag, InitRamStartPhaseTag)

    def process(self):
        remove_boot_entry()
