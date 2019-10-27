#!/usr/bin/env python3

import argparse as arp

def make_parser():

    prs = arp.ArgumentParser()

    parser = arp.ArgumentParser()

    subparsers = parser.add_subparsers(dest = 'command')
    run_parser = subparsers.add_parser("run")
    look_parser = subparsers.add_parser("look")

# Run Parser Arguments ---------------------------------------------

    run_parser.add_argument('-scc','--sc_cnt',
                        required = False,
                        type = str,
                        help = ''.join(["path to single cell",
                                       " count file. Should be",
                                       " on format n_cells x n_genes",
                                       " use flag sct to transpose if",
                                       " if necessary"]))

    run_parser.add_argument('-scl','--sc_labels',
                        required = False,
                        type = str,
                        help = ''.join(["path to single cell",
                                        " labels file. Should be on",
                            ]))

    run_parser.add_argument('-lcn','--label_colname',
                        required = False,
                        default = 'bio_celltype',
                        type = str,
                        help = ''.join(["name of columns that",
                                        " cell type labels are",
                                        " listed",
                            ]))


    run_parser.add_argument('-scb','--sc_batch_size',
                        required = False,
                        default = None,
                        type = int,
                        help = ''.join(["batch size for",
                                        " single cell data set",
                            ]))

    run_parser.add_argument('-stc','--st_cnt',
                        required = False,
                        nargs = '+',
                        help = ''.join(["path to spatial",
                               " transcriptomics count file.",
                               " Shoul be on form",
                               " n_spots x n_genes"]))

    run_parser.add_argument('-stm','--st_model',
                        default = None,
                        required = False,
                        help = ''.join(["path to already fitted",
                                       " st model"]))

    run_parser.add_argument('-scm','--sc_model',
                        required = False,
                        default = None,
                        help = ''.join(["path to already fitted",
                                       " sc model"]))


    run_parser.add_argument('-sce','--sc_epochs',
                        required = False,
                        default = 20000,
                        type = int,
                        help = ''.join(["number of epochs",
                                " to be used in fitting",
                                " of single cell data.",
                                " Default is set to 2e4",
                                ]))


    run_parser.add_argument('-stb','--st_batch_size',
                        required = False,
                        default = None,
                        type = int,
                        help = ''.join(["batch size for",
                               " st data set",
                               ]))

    run_parser.add_argument('-scf','--sc_fit',
                        required = False,
                        default = [None,None],
                        nargs = 2,
                        help =''.join(["parameters fitted",
                                       " from single cell",
                                       " data. First argument",
                                       " should be path to",
                                       " R-matrix and second",
                                       " to logit vector"])
                               )


    run_parser.add_argument('-ste','--st_epochs',
                        default = 20000,
                        type = int,
                        help = ''.join(["number of epochs",
                                " to be used in fitting",
                                " of spatial transcriptomics",
                                " data.",
                                " Default is set to 2e4",
                                ]))

    run_parser.add_argument('-o','--out_dir',
                        required = False,
                        default = '',
                        type = str,
                        help = ''.join([" full path to output",
                                        " directory. Files will",
                                        " be saved with standard ",
                                        " name and timestamp",
                                        ]))

    run_parser.add_argument('-shh','--silent_mode',
                        required = False,
                        default = False,
                        action = 'store_true',
                        help = ''.join(["include to silence",
                                        "output throughout",
                                        "fitting",
                                        ]))

    run_parser.add_argument('-n','--topn_genes',
                        required = False,
                        default = None,
                        type = int,
                        help = ''.join(["only use top n",
                                        " mose highly expressed",
                                        " genes"
                                        ]))


    run_parser.add_argument('-fg','--filter_genes',
                        required = False,
                        default = False,
                        action = 'store_true',
                        help = ''.join([f"Filter Ribosomal Genes",
                                        f" and MALAT1",
                                        ]))


    run_parser.add_argument("-lr","--learning_rate",
                        required = False,
                        default = 0.01,
                        type = float,
                        help = ''.join([f"learning rate to be",
                                        f" used."
                                        ]))


    run_parser.add_argument("-mscc","--min_sc_counts",
                        required = False,
                        default = 300,
                        type = float,
                        help = ''.join([f"minimum number of ",
                                        f" counts for single cells",
                                        f" to be included in",
                                        f" the analysis",
                                        ]))

    run_parser.add_argument("-mstc","--min_st_counts",
                        required = False,
                        default = 0,
                        type = float,
                        help = ''.join([f"minimum number of ",
                                        f" counts for single cells",
                                        f" to be included in",
                                        f" the analysis",
                                        ]))


    run_parser.add_argument("-mc","--min_cells",
                        required = False,
                        default = 0.0,
                        type = float,
                        help = ''.join([f"minimum number of ",
                                        f" cells for genes",
                                        f" to be observed in",
                                        f" the analysis",
                                        ]))

    run_parser.add_argument("-ms","--min_spots",
                        required = False,
                        default = 0.0,
                        type = float,
                        help = ''.join([f"minimum number of ",
                                        f" spots for genes",
                                        f" to be observed in",
                                        f" the analysis",
                                        ]))


    run_parser.add_argument('-gp','--gpu',
                        required = False,
                        default = False,
                        action = 'store_true',
                        help = ''.join(["use gpu",
                                        ]))

    run_parser.add_argument('-gl','--gene_list',
                        required = False,
                        default = None,
                        type = str,
                        help = ''.join(["path to list of genes",
                                        " to use",
                                        ]))



# Look Parser Arguments -----------------------------------------------

    look_parser.add_argument("-pp","--proportions_path",
                        type = str,
                        nargs = '+',
                        required = True,
                        help = ''.join([f"Path to proportions",
                                       f" file generated by",
                                       f" st2sc. Named W*.tsv"])
                                       )


    look_parser.add_argument("-c","--compress_method",
                        type = str,
                        required = False,
                        default = None,
                        help = ''.join([f"method to be used",
                                        f" for compression of",
                                        f" information."]),
                                       )

    look_parser.add_argument("-ms","--marker_size",
                        type = int,
                        required = False,
                        default = 100,
                        help = ''.join([f"size of scatterplot",
                                        f" markers. Default 100"
                                        ]))

    look_parser.add_argument("-o","--output",
                        type = str,
                        required = False,
                        default = '',
                        help = ''.join([f"Path to output",
                                        f" can either be",
                                        f" a directory or",
                                        f" filename. If only",
                                        f" dir is given, same",
                                        f" basename os for pp",
                                        f" is used."])
                               )

    look_parser.add_argument("-nc","--n_cols",
                        default = 2,
                        type = int,
                        required = False,
                        )

    look_parser.add_argument("-y","--flip_y",
                        required = False,
                        default = False,
                        action = 'store_true',
                        )

    look_parser.add_argument("-sb","--sort_by",
                        required = False,
                        default = 'ct',
                        type = str)

    look_parser.add_argument("-sc","--scale_by",
                        required = False,
                        default = 'ct',
                        type = str)


    look_parser.add_argument("-gb","--gathered_compr",
                        required = False,
                        default = False,
                        action = 'store_true',
                        )

    look_parser.add_argument("-sf","--scaling_factor",
                        required = False,
                        type = float,
                        default = 4.0,
                        help = ''.join([]),
                        )

    look_parser.add_argument("-hu","--hue_rotate",
                        required = False,
                        type = float,
                        default = -1.0,
                        help = ''.join([]),
                        )


    look_parser.add_argument("-hex","--hexagonal",
                        required = False,
                        default = False,
                        action = 'store_true',
                        help = ''.join([]),
                        )

    look_parser.add_argument("-shu","--shuffle_rgb",
                        required = False,
                        default = False,
                        action = 'store_true',
                        help = ''.join(["Shuffle RGB colors",
                                        " in the compressed",
                                        " visualization",
                                       ]),
                        )


    return parser
