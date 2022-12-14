from utils import load_filepaths

import argparse
from ensemble.pseudolabels_ensemble import make_modelwise_submission_ensemble, \
    make_columnwise_submission_ensemble, \
    make_columnwise_submission_ensemble2
import os

ensemble_weights = {
    'ensemble_44631': {
        'model20': 0.6,
        'model19': 0.25,
        'model18': 0.15
    },
    'ensemble_4459': {
        'model21': 0.5,
        'model20': 0.275,
        'model19': 0.125,
        'model18': 0.1
    },
    'ensemble_4449': {
        'model17': 0.10891375279,
        'model18': 0.01085920545,
        'model19': 0.00193970403,
        'model20': 0.04376893255,
        'model21': 0.11835317182,
        'model22': 0.01386750842,
        'model23': 0.32875780112,
        'model24': 0.18492612482,
        'model29': 0.18861379895,
    },
    'ensemble_4448': {
        'model17': 0.10822125192240414,
        'model18': 0.0,
        'model19': 0.0,
        'model20': 0.01027712179022292,
        'model21': 0.08334036355017828,
        'model22': 0.02274617932455912,
        'model23': 0.21521827833060778,
        'model24': 0.13176402908375676,
        'model29': 0.17266452988372935,
        'model30': 0.2549639506239497
    },
    'ensemble_4447': {
        'model17': 0.0962165959606631,
        'model18': 3.3316650416041794e-17,
        'model19': 0.0,
        'model20': 9.03994642832288e-18,
        'model21': 0.08655741486749564,
        'model22': 9.974659986866641e-18,
        'model23': 0.17080959770461437,
        'model24': 0.0004322681398924201,
        'model29': 0.12217267050944432,
        'model30': 0.10167456460974643,
        'model31': 0.2153011130526323,
        'model32': 0.20563589072767532
    },
    'ensemble_44439': {
        'model2': 0.12080487996851937,
        'model17': 0,
        'model18': 0,
        'model19': 0,
        'model20': 0.002515966147924016,
        'model21': 0.06066129221356339,
        'model22': 0.004367412946160462,
        'model23': 0.22956412946160462,
        'model24': 0,
        'model27': 0.024874241779985446,
        'model28': 0.0015581526028578495,
        'model29': 0.02924511095662808,
        'model30': 0.12292821031369401,
        'model31': 0.11962654518496374,
        'model32': 0.13369399467504667,
        'model33': 0,
        'model34': 0,
        'model35': 0.14939736107378382,
    },
    'ensemble_444371': {
        'model2': 0.104568927986581,
        'model17': 0,
        'model18': 0,
        'model19': 0,
        'model20': 0.00396867158276209,
        'model21': 0.07197941480535167,
        'model22': 0.,
        'model23': 0.20794739304083878,
        'model24': 0.001224549812895024,
        'model27': 0.014124900674815893,
        'model28': 0.,
        'model29': 0.02283341828675994,
        'model30': 0.1266942077585073,
        'model31': 0.07299788992081675,
        'model32': 0.13555597715368523,
        'model33': 0.,
        'model34': 0.,
        'model35': 0.05330993459916873,
        'model36': 0.08066604837747007,
        'model37': 0.10330986929079802,
    },
    'ensemble_444335': {
        'model2': 0.1029042833387868,
        'model17': 0.0,
        'model18': 1.9058659460380317e-17,
        'model19': 0.0,
        'model20': 4.2536623615725803e-19,
        'model21': 0.07518296172317124,
        'model22': 0.0,
        'model23': 0.1964491406113391,
        'model24': 1.857472786034887e-18,
        'model27': 6.5052130349130266e-18,
        'model28': 0.0,
        'model29': 0.006570626757716589,
        'model30': 0.1261884004753692,
        'model31': 0.08625332610586658,
        'model32': 0.07773571046756915,
        'model33': 3.469446951953614e-18,
        'model34': 0.0004872993659464684,
        'model35': 0.021777790638685145,
        'model36': 0.0759830773537634,
        'model37': 0.09247660399523161,
        'model38': 1.3612939556721994e-18,
        'model39': 0.08872012240370862,
        'model40': 2.5410540923128933e-18,
        'model41': 0.0,
        'model43': 0.048674170418083196,
        'model44': 0.0
    },
    'ensemble_4419': {'cohesion': {'model2': 0.0,
                                   'model17': 1.3641303991688677e-18,
                                   'model18': 3.3687184734861214e-18,
                                   'model19': 2.35113150999648e-18,
                                   'model20': 0.0,
                                   'model21': 0.014721199316359353,
                                   'model22': 0.20079267640478035,
                                   'model23': 0.10727387089983963,
                                   'model24': 1.4571673548843897e-18,
                                   'model27': 0.0,
                                   'model28': 0.0,
                                   'model29': 0.04321860279406503,
                                   'model30': 0.0,
                                   'model31': 0.15261620075515803,
                                   'model32': 0.0,
                                   'model33': 0.02726037390160297,
                                   'model34': 1.3615815440454913e-20,
                                   'model35': 0.0,
                                   'model36': 0.0,
                                   'model37': 0.0,
                                   'model38': 5.4158895657244366e-18,
                                   'model39': 0.0,
                                   'model40': 1.860853272557901e-18,
                                   'model41': 2.3550298541923315e-18,
                                   'model43': 0.0,
                                   'model44': 0.0,
                                   'model45': 6.732399217305961e-19,
                                   'model46': 0.0,
                                   'model47': 2.8946693581574397e-18,
                                   'model48': 0.0,
                                   'model49': 0.08490032272754919,
                                   'model50': 0.0,
                                   'exp01_fb3': 0.0010949994243920824,
                                   'exp01_fb3_part2': 2.2434177521021126e-18,
                                   'exp02_fb3': 0.0726923366270686,
                                   'exp02_fb3_part2_distilbart': 0.007237901334420236,
                                   'exp02_fb3_part2_distilbert': 0.03455879417868948,
                                   'exp03_fb3': 1.5437240657547322e-19,
                                   'exp04_fb3': 0.043031824405246936,
                                   'exp12_fb3': 0.012011623224385225,
                                   'exp13_fb3': 0.06440109372972913,
                                   'exp14_fb3_deberta': 0.0198808828346093,
                                   'exp14_fb3_roberta': 0.11267501305350522},
                      'syntax': {'model2': 0.0,
                                 'model17': 1.734723475976807e-18,
                                 'model18': 0.0,
                                 'model19': 4.290871407780592e-19,
                                 'model20': 0.03419437366866644,
                                 'model21': 0.1621238531338363,
                                 'model22': 2.006322991748364e-18,
                                 'model23': 0.1160414494705781,
                                 'model24': 0.0,
                                 'model27': 0.0,
                                 'model28': 0.04468067771630145,
                                 'model29': 0.0,
                                 'model30': 0.0,
                                 'model31': 7.985004705580017e-18,
                                 'model32': 6.4293462147500905e-18,
                                 'model33': 4.1444423669479873e-19,
                                 'model34': 0.0,
                                 'model35': 0.0,
                                 'model36': 6.208155622140726e-18,
                                 'model37': 0.05531490985121265,
                                 'model38': 6.015386165335163e-19,
                                 'model39': 3.563162343550345e-18,
                                 'model40': 2.584740732259664e-19,
                                 'model41': 3.70880069133413e-21,
                                 'model43': 0.0038943403140923112,
                                 'model44': 0.0,
                                 'model45': 0.0,
                                 'model46': 1.2915975153876891e-18,
                                 'model47': 0.0,
                                 'model48': 0.0,
                                 'model49': 5.9264284748402e-19,
                                 'model50': 0.0,
                                 'exp01_fb3': 0.0,
                                 'exp01_fb3_part2': 0.09423395310886282,
                                 'exp02_fb3': 0.10103229579773294,
                                 'exp02_fb3_part2_distilbart': 0.0,
                                 'exp02_fb3_part2_distilbert': 1.236070928715173e-19,
                                 'exp03_fb3': 0.05026367797777125,
                                 'exp04_fb3': 0.08142772437504354,
                                 'exp12_fb3': 0.054632911276372306,
                                 'exp13_fb3': 0.10922481001240171,
                                 'exp14_fb3_deberta': 0.0,
                                 'exp14_fb3_roberta': 0.09160329705548483},
                      'vocabulary': {'model2': 6.384581712459615e-18,
                                     'model17': 0.0,
                                     'model18': 0.0,
                                     'model19': 3.363060494262179e-19,
                                     'model20': 0.0,
                                     'model21': 0.0,
                                     'model22': 0.0,
                                     'model23': 0.15151296054051305,
                                     'model24': 0.0,
                                     'model27': 9.540979117872439e-18,
                                     'model28': 0.0,
                                     'model29': 0.0,
                                     'model30': 0.11111887475408921,
                                     'model31': 1.017773877800927e-17,
                                     'model32': 0.12930318094216392,
                                     'model33': 0.0,
                                     'model34': 0.0,
                                     'model35': 0.0,
                                     'model36': 0.0,
                                     'model37': 8.464107105309035e-19,
                                     'model38': 0.0,
                                     'model39': 0.030982732857463224,
                                     'model40': 8.730541746025401e-19,
                                     'model41': 0.0,
                                     'model43': 0.06299261994832991,
                                     'model44': 2.0558298615489533e-18,
                                     'model45': 1.430788180522078e-18,
                                     'model46': 5.6107462426124854e-18,
                                     'model47': 0.0,
                                     'model48': 2.079844836422999e-18,
                                     'model49': 0.0,
                                     'model50': 5.113870540624896e-19,
                                     'exp01_fb3': 0.0,
                                     'exp01_fb3_part2': 0.0,
                                     'exp02_fb3': 0.11591427762755883,
                                     'exp02_fb3_part2_distilbart': 0.032512192260639956,
                                     'exp02_fb3_part2_distilbert': 0.012237994247405837,
                                     'exp03_fb3': 0.03132175809822703,
                                     'exp04_fb3': 0.08313984648412528,
                                     'exp12_fb3': 0.12170917967553489,
                                     'exp13_fb3': 0.05967899610352756,
                                     'exp14_fb3_deberta': 0.015818441570440357,
                                     'exp14_fb3_roberta': 0.04178084716540002},
                      'phraseology': {'model2': 0.061881001168637303,
                                      'model17': 1.362926360355619e-18,
                                      'model18': 0.0,
                                      'model19': 2.8535932787121293e-18,
                                      'model20': 0.0,
                                      'model21': 7.14753724821551e-18,
                                      'model22': 0.0,
                                      'model23': 0.08725123253206267,
                                      'model24': 9.270763313379683e-19,
                                      'model27': 1.1693805745033369e-18,
                                      'model28': 2.173169471139076e-18,
                                      'model29': 0.0,
                                      'model30': 0.0788119343114915,
                                      'model31': 0.0,
                                      'model32': 0.002363552255962262,
                                      'model33': 1.2356697873140099e-18,
                                      'model34': 4.2658844213293216e-19,
                                      'model35': 0.0,
                                      'model36': 5.421010862427522e-19,
                                      'model37': 0.0,
                                      'model38': 2.2862213791092874e-18,
                                      'model39': 7.912096156176944e-20,
                                      'model40': 0.050759096717978874,
                                      'model41': 1.7603243955161548e-18,
                                      'model43': 0.025591136694847093,
                                      'model44': 0.0,
                                      'model45': 0.0,
                                      'model46': 0.0,
                                      'model47': 4.0880205125975284e-19,
                                      'model48': 1.4049467362816434e-18,
                                      'model49': 1.1948309598070998e-18,
                                      'model50': 1.653260234299397e-18,
                                      'exp01_fb3': 2.7733638123011357e-18,
                                      'exp01_fb3_part2': 0.13110749023836157,
                                      'exp02_fb3': 0.018897104991641992,
                                      'exp02_fb3_part2_distilbart': 0.03985037310976023,
                                      'exp02_fb3_part2_distilbert': 0.052104546030576,
                                      'exp03_fb3': 1.6410002556183483e-18,
                                      'exp04_fb3': 0.2869354561758461,
                                      'exp12_fb3': 0.04195254942891115,
                                      'exp13_fb3': 0.12144418876602656,
                                      'exp14_fb3_deberta': 0.000620852697738587,
                                      'exp14_fb3_roberta': 0.0},
                      'grammar': {'model2': 9.080250388890479e-18,
                                  'model17': 2.0634939360973545e-18,
                                  'model18': 1.9767107116602035e-18,
                                  'model19': 0.0,
                                  'model20': 0.0,
                                  'model21': 0.05858274048806288,
                                  'model22': 1.3023529903539446e-18,
                                  'model23': 0.06851055940284298,
                                  'model24': 7.126553420297553e-18,
                                  'model27': 4.756212570122803e-19,
                                  'model28': 1.0519000963689585e-17,
                                  'model29': 0.0,
                                  'model30': 0.0,
                                  'model31': 0.0,
                                  'model32': 1.667373442397137e-18,
                                  'model33': 0.0,
                                  'model34': 0.0,
                                  'model35': 0.014386516923729055,
                                  'model36': 0.01602923044602552,
                                  'model37': 0.0,
                                  'model38': 0.0632552136055105,
                                  'model39': 0.0,
                                  'model40': 0.0,
                                  'model41': 2.307494908013121e-18,
                                  'model43': 0.0026822888246185467,
                                  'model44': 0.0,
                                  'model45': 0.23047446295313717,
                                  'model46': 1.4563320421899575e-19,
                                  'model47': 0.0,
                                  'model48': 0.0284030791866702,
                                  'model49': 0.0,
                                  'model50': 1.265480985157968e-18,
                                  'exp01_fb3': 0.0,
                                  'exp01_fb3_part2': 0.23375101401803414,
                                  'exp02_fb3': 0.042024852615124626,
                                  'exp02_fb3_part2_distilbart': 0.027760075178077666,
                                  'exp02_fb3_part2_distilbert': 0.003586179954204018,
                                  'exp03_fb3': 0.0,
                                  'exp04_fb3': 0.0,
                                  'exp12_fb3': 0.0014210081478568258,
                                  'exp13_fb3': 0.13387900083046145,
                                  'exp14_fb3_deberta': 0.07427526019738938,
                                  'exp14_fb3_roberta': 2.231943155272213e-18},
                      'conventions': {'model2': 0.0,
                                      'model17': 1.0611962407261138e-17,
                                      'model18': 4.091194453525049e-18,
                                      'model19': 3.1796999780611212e-18,
                                      'model20': 0.05421467691981856,
                                      'model21': 0.11235702311902371,
                                      'model22': 0.03685431192438295,
                                      'model23': 0.08348152741662603,
                                      'model24': 6.705392197469761e-18,
                                      'model27': 0.0,
                                      'model28': 0.0,
                                      'model29': 2.2565293333723027e-18,
                                      'model30': 0.03711650173217246,
                                      'model31': 0.07960785607315367,
                                      'model32': 0.0,
                                      'model33': 5.854734912756549e-20,
                                      'model34': 6.534591974053476e-19,
                                      'model35': 2.2707543095078078e-18,
                                      'model36': 1.781157642930368e-18,
                                      'model37': 0.0004151450021269716,
                                      'model38': 2.3250822209596838e-18,
                                      'model39': 8.084792747254291e-18,
                                      'model40': 0.0,
                                      'model41': 0.0,
                                      'model43': 0.0,
                                      'model44': 1.8084786498765856e-18,
                                      'model45': 0.026210720906841286,
                                      'model46': 0.0,
                                      'model47': 5.86831289833729e-18,
                                      'model48': 0.0,
                                      'model49': 1.3025745570576695e-18,
                                      'model50': 0.0,
                                      'exp01_fb3': 1.7163569512729368e-18,
                                      'exp01_fb3_part2': 0.3307626748306759,
                                      'exp02_fb3': 4.622663978172529e-18,
                                      'exp02_fb3_part2_distilbart': 0.009619658189335517,
                                      'exp02_fb3_part2_distilbert': 0.014871211144167468,
                                      'exp03_fb3': 0.06376301869148857,
                                      'exp04_fb3': 0.028266178548082305,
                                      'exp12_fb3': 0.04133052338175039,
                                      'exp13_fb3': 0.03381778391813708,
                                      'exp14_fb3_deberta': 0.0,
                                      'exp14_fb3_roberta': 0.04863975850957641}},
    'current_train_ensemble_4434': {'cohesion': {'model21': 0.0,
                                                 'model23': 0.16857263892568816,
                                                 'model30': 5.6466451698871394e-18,
                                                 'model31': 0.12849541458592756,
                                                 'model37': 0.03751041415777451,
                                                 'model43': 0.07091293069690112,
                                                 'model45': 9.608947831724199e-19,
                                                 'model52': 0.5922561202068483},
                                    'syntax': {'model21': 0.2983559500041119,
                                               'model23': 0.039662915900296386,
                                               'model30': 3.6904749955145715e-17,
                                               'model31': 0.0,
                                               'model37': 0.13482866262881374,
                                               'model43': 0.04065192941186354,
                                               'model45': 0.0,
                                               'model52': 0.48574664922632727},
                                    'vocabulary': {'model21': 3.7173705316985325e-18,
                                                   'model23': 0.22752938119344748,
                                                   'model30': 0.22659113445015197,
                                                   'model31': 1.4990253051788373e-18,
                                                   'model37': 0.07948298439524726,
                                                   'model43': 0.10250239273559535,
                                                   'model45': 2.66102757507777e-18,
                                                   'model52': 0.36390845133777716},
                                    'phraseology': {'model21': 2.0637794141115326e-18,
                                                    'model23': 0.14103588237240658,
                                                    'model30': 0.0928342567553126,
                                                    'model31': 1.571572127235293e-18,
                                                    'model37': 0.08452575674341647,
                                                    'model43': 0.07343995419462711,
                                                    'model45': 0.0,
                                                    'model52': 0.6081277882951115},
                                    'grammar': {'model21': 0.10336485339119193,
                                                'model23': 0.0,
                                                'model30': 0.042336648911786706,
                                                'model31': 2.5720590269845573e-19,
                                                'model37': 0.10176675182405476,
                                                'model43': 1.0297838170757434e-19,
                                                'model45': 0.0777058421524695,
                                                'model52': 0.6731450757163463},
                                    'conventions': {'model21': 0.020538210645085504,
                                                    'model23': 0.19011204334494136,
                                                    'model30': 0.0007462543700502877,
                                                    'model31': 0.03245091359272288,
                                                    'model37': 0.06218846281441917,
                                                    'model43': 0.0,
                                                    'model45': 9.687721117741096e-18,
                                                    'model52': 0.6922934794192225}}
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ensemble_id', type=str)
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_args()
    filepaths = load_filepaths()

    ensemble_ids_list = list(ensemble_weights.keys())
    assert args.ensemble_id in ensemble_ids_list, f'Ensemble id should be one of [{ensemble_ids_list}]'

    pseudolabels_path = filepaths['PREVIOUS_DATA_PSEUDOLABELS_DIR_PATH']
    if args.ensemble_id == 'current_train_ensemble_4434':
        pseudolabels_path = filepaths['CURRENT_DATA_PSEUDOLABELS_DIR_PATH']

    model_weights = ensemble_weights[args.ensemble_id]
    output_dir = os.path.join(pseudolabels_path, f'{args.ensemble_id}_pseudolabels')
    if args.ensemble_id == 'current_train_ensemble_4434':
        output_dir = os.path.join(pseudolabels_path, f'{args.ensemble_id.replace("current_train_", "")}_pseudolabels')

    if args.ensemble_id == 'ensemble_4419':
        make_columnwise_submission_ensemble(pseudolabels_path=pseudolabels_path,
                                            model_weights=model_weights,
                                            output_dir=output_dir)
    elif args.ensemble_id == 'current_train_ensemble_4434':
        make_columnwise_submission_ensemble2(filepaths,
                                             pseudolabels_path=pseudolabels_path,
                                             model_weights=model_weights,
                                             output_dir=output_dir)
    else:
        make_modelwise_submission_ensemble(pseudolabels_path=pseudolabels_path,
                                           model_weights=model_weights,
                                           output_dir=output_dir)
