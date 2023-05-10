from tethys_sdk.base import TethysAppBase


class HydroviewerEcuador(TethysAppBase):
    """
    Tethys app class for Hydroviewer Ecuador.
    """

    name = 'Hydroviewer Ecuador'
    description = ''
    package = 'hydroviewer_ecuador'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'hydroviewer-ecuador'
    color = '#20295c'
    tags = ''
    enable_feedback = False
    feedback_emails = []